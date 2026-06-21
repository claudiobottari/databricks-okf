---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eafbfe74201d4490e653c34d5d4c76109b82142eb088c645bed22140e8cec597
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - to-and-except-clauses-for-principal-targeting-in-abac
    - EXCEPT Clauses for Principal Targeting in ABAC and TO
    - TAECFPTIA
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: TO and EXCEPT Clauses for Principal Targeting in ABAC
description: Using TO and EXCEPT clauses in row filter, column mask, and GRANT policies to define which users and groups policies apply to, keeping UDF logic simpler.
tags:
  - attribute-based-access-control
  - policy-design
timestamp: "2026-06-19T17:40:42.384Z"
---

# TO and EXCEPT Clauses for Principal Targeting in ABAC

**TO and EXCEPT Clauses for Principal Targeting in ABAC** are mechanisms used in [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies on Databricks to specify which users and groups a policy applies to or excludes from. These clauses are part of row filter and column mask policy definitions, and they help keep policy logic simple by separating principal targeting from data transformation logic.

## Overview

In ABAC policies, the `TO` clause defines which principals (users and groups) the policy applies to, while the `EXCEPT` clause excludes specific principals from the policy entirely. When a principal is excluded via `EXCEPT`, they are not subject to any filtering or masking that the policy would otherwise apply. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Benefits

Using `TO` and `EXCEPT` clauses keeps the underlying UDF (user-defined function) logic simple. Instead of embedding complex conditional logic about which users should be affected within the UDF itself, the principal targeting is handled declaratively at the policy level. This separation of concerns makes policies easier to understand, maintain, and audit. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Usage in Row Filters and Column Masks

For [Row Filter Policies](/concepts/row-filter-policies.md) and [Column Mask Policies](/concepts/column-mask-policies.md), the `TO` and `EXCEPT` clauses are the preferred approach for defining which users and groups the policy applies to. This is recommended over embedding identity functions like `is_account_group_member()` inside UDFs, though those remain a valid option when complex conditional logic is required. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Usage in GRANT Policies

For [ABAC GRANT Policies](/concepts/abac-grant-policies.md) (Beta), `TO` and `EXCEPT` are the only mechanisms available for targeting principals. Unlike row filters and column masks, GRANT policies do not use UDFs, so the `TO` and `EXCEPT` clauses are the sole way to specify which principals receive the granted privileges. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Best Practices

- **Prefer TO/EXCEPT over UDF-based logic**: Use the policy's `TO` and `EXCEPT` clauses to define principal targeting whenever possible. This keeps UDF logic focused on data transformation rather than access control. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Use EXCEPT for exemptions**: The `EXCEPT` clause is specifically designed to exclude certain users from a policy entirely, so they see unfiltered or unmasked data. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Reserve UDF-based logic for complex cases**: When conditional logic based on user attributes is too complex for simple `TO`/`EXCEPT` clauses, identity functions like `is_account_group_member()` inside UDFs remain a valid option. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Row Filter Policies](/concepts/row-filter-policies.md)
- [Column Mask Policies](/concepts/column-mask-policies.md)
- [ABAC GRANT Policies](/concepts/abac-grant-policies.md)
- ABAC Policy Design Best Practices
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)

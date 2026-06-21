---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5fc63db16cb6e05ad84f74d569ad769a226f8d6f11e6be893d28916e119b8b2e
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-grant-policies-and-direct-grants-auditing
    - Direct Grants Auditing and ABAC GRANT Policies
    - AGPADGA
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: ABAC GRANT Policies and Direct Grants Auditing
description: Auditing both direct grants and ABAC GRANT policies together to uncover unintended permissions
tags:
  - data-governance
  - abac
  - auditing
  - unity-catalog
timestamp: "2026-06-19T22:13:24.763Z"
---

# ABAC GRANT Policies and Direct Grants Auditing

**ABAC GRANT Policies and Direct Grants Auditing** refers to the practice of reviewing both attribute-based access control (ABAC) GRANT policies and traditional direct grants to understand the effective privileges that principals hold on Unity Catalog securable objects. Because a user's effective privileges are the union of both sources, auditing only one surface can hide unintended permissions. ^[best-practices-for-abac-policies-databricks-on-aws.md] See [ABAC GRANT Policies](/concepts/abac-grant-policies.md) for details on the policy mechanism.

## Why Audit Both

ABAC GRANT policies (Beta) dynamically grant privileges to securable objects whose governed tags match a condition. Direct grants, by contrast, enumerate privileges explicitly on named objects or their ancestors. A principal may hold `EXECUTE` on a model through an ABAC GRANT policy, a direct grant on the model itself, an inherited direct grant from its parent schema or catalog, or a combination of these. Auditing only direct grants risks overlooking access that a GRANT policy provides — and vice versa. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Understanding the Union of Effective Privileges

The effective privileges on an object are the union of all applicable ABAC GRANT policies and all direct grants. For a given privilege and securable, a principal holds the privilege if any of the following is true:

- An ABAC GRANT policy attached to the securable's catalog or schema lists the principal in `TO` (and not in `EXCEPT`) and the policy's `WHEN` condition matches the tags on the securable. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- A direct `GRANT` of that privilege exists on the securable, its schema, or its catalog, whether granted directly, through group membership, or through other administrative privileges. ^[best-practices-for-abac-policies-databricks-on-aws.md]

Because access is the union, a restrictive GRANT policy does not by itself guarantee that an excluded principal lacks the privilege — the principal may still hold it through a direct grant. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Methods for Auditing

Auditing requires checking both policy-based and direct privilege sources. The following tools are available depending on the securable type and level of detail needed.

### Inspect Effective Policies

Use `SHOW EFFECTIVE POLICIES` to determine which ABAC GRANT policies apply to a given securable object and whether they are inherited from parent scopes. This command lists every GRANT policy whose scope covers the object, including those inherited from a catalog when querying a schema. ^[best-practices-for-abac-policies-databricks-on-aws.md]

For models (the only securable currently supported by ABAC GRANT policies), the command is:

```sql
SHOW EFFECTIVE POLICIES ON SCHEMA <parent_schema>
```

The equivalent REST API (`GET /api/2.1/unity-catalog/policies/{on_securable_type}/{on_securable_fullname}?include_inherited=true`) and Python SDK (`w.policies.list_policies(..., include_inherited=True)`) return the same information.

### Inspect Direct Grants

Use `SHOW GRANTS` on the securable object and its ancestors to enumerate direct grants. The REST API for direct grants on a specific securable is `GET /api/2.1/unity-catalog/permissions/{securable_type}/{full_name}` (Python SDK: `w.grants.get()`). To see the union of direct and inherited grants, use `GET /api/2.1/unity-catalog/effective-permissions/{securable_type}/{full_name}` (Python SDK: `w.grants.get_effective()`). ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Best Practices for Auditing

- **Audit direct grants and ABAC GRANT policies together.** When reviewing access, check both surfaces. Auditing only one can hide unintended permissions. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Use groups in `TO` and `EXCEPT` clauses.** Adding or removing users from a group changes who the policy applies to without editing the policy, simplifying future audits. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Document the tagging taxonomy and policy definitions.** Because policies evaluate dynamically at query time based on tags and identity, maintaining clear documentation helps data consumers and auditors understand which rules apply. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Consider table-level row filters and column masks for transparency.** If a specific object requires explicit, directly visible access rules, use those mechanisms instead of ABAC policies, ensuring no conflicts arise. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related Concepts

- [ABAC GRANT Policies](/concepts/abac-grant-policies.md) — The attribute-based access control mechanism that dynamically grants privileges based on tags
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The full set of securable actions and grantable privileges
- [Governed Tags](/concepts/governed-tags.md) — Tags used in ABAC GRANT policy conditions
- [Row Filter Policies](/concepts/row-filter-policies.md) and [Column Mask Policies](/concepts/column-mask-policies.md) — Other ABAC policy types that restrict data content rather than access
- ABAC vs. Row Filters and Column Masks — Choosing between policy types
- ABAC Policy Performance — Authorization check costs with many policies

## Sources

- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)

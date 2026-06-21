---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2aa2fdbdf6ace163f6f2a7279054856bd02660a42fefd39e2ddde0c62db9e1fd
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dynamic-abac-policy-evaluation
    - DAPE
    - ABAC Policy Evaluation
    - ABAC policy evaluation
    - Dynamic policy evaluation
    - Policy Evaluation
    - Tag-based policy evaluation
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: Dynamic ABAC Policy Evaluation
description: ABAC policies evaluate at query time based on user identity, group memberships, and object tags, requiring tools like SHOW EFFECTIVE POLICIES and documentation for transparency.
tags:
  - abac
  - dynamic-evaluation
  - transparency
timestamp: "2026-06-18T14:32:50.422Z"
---

---

# Dynamic ABAC Policy Evaluation

**Dynamic ABAC Policy Evaluation** is a core characteristic of [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) in [Unity Catalog](/concepts/unity-catalog.md). Unlike static row filters and column masks that are directly visible on a table definition, ABAC policies are evaluated at query time based on the user's identity and group memberships, and the tags on the data object in the policy scope. This dynamic nature means that the access rules applying to a given table can change depending on who is querying it and what tags are currently applied. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Overview

ABAC policies are evaluated dynamically because they rely on runtime attributes—the principal's identity and group memberships, and the governed tags on the securable object—rather than on a static list of grants. This means that a single data object can be subject to different policies for different users, and that adding or removing a tag from an object can immediately change which policies apply to it. ^[best-practices-for-abac-policies-databricks-on-aws.md]

This dynamic evaluation is a key difference between ABAC policies and [Table-Level Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md), which are defined directly on the table schema and are visible as part of the table definition. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Why Dynamic Evaluation Matters

Dynamic evaluation has important implications for both data consumers and data owners:

- **For data consumers:** A user querying the same table as another user may see different rows or different column values, depending on their own group memberships and the tags on the data they are accessing. This can make it harder to understand which access rules apply to a given query. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- **For data owners:** Changing a tag on a data object (for example, changing the `sensitivity` tag from `internal` to `confidential`) can immediately change which policies apply to that object. This enables governance to be managed through tag assignment rather than through individual grant statements. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Managing Dynamic Evaluation

Because ABAC policies are dynamic, teams should take proactive steps to manage and understand their impact:

1. **Document the tagging taxonomy and policies.** A clear, shared understanding of the tag key names, allowed values, and the policies that reference them helps all teams understand the governance model without having to inspect each policy individually. ^[best-practices-for-abac-policies-databricks-on-aws.md]
2. **Use `SHOW EFFECTIVE POLICIES`** to determine which policies apply to a specific table for a given user. This command reveals the policies that are in effect at query time, accounting for both directly-attached policies and those inherited from parent scopes. ^[best-practices-for-abac-policies-databricks-on-aws.md]
3. **Audit both direct grants and ABAC GRANT policies together.** Because a user's effective privileges on a data object are the union of both direct grants and ABAC GRANT policies, auditing only one surface can hide unintended permissions. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Transparency vs. Dynamic Policy Evaluation

There is a trade-off between transparency and dynamic policy evaluation. For cases where transparency is critical for a specific table, consider using [Table-Level Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) for that isolated case instead of relying on ABAC policies. However, before doing so, ensure that any potential conflicts between the table-level policy and the broader ABAC policies are addressed. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related Concepts

- [ABAC GRANT Policies](/concepts/abac-grant-policy.md) — Dynamically grant privileges based on matching tags
- [Row Filter Policies](/concepts/row-filter-policies.md) — ABAC policies that restrict data content
- [Column Mask Policies](/concepts/column-mask-policies.md) — ABAC policies that mask sensitive columns
- [Table-Level Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) — Static filters defined on the table definition
- [Governed Tags](/concepts/governed-tags.md) — Tags used in policy conditions
- [SHOW EFFECTIVE POLICIES](/concepts/show-effective-policies.md) — Command to determine which policies apply

## Sources

- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)

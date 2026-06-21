---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c5ec18cf2c5ac77d16a4b3a711b8f888e220996b9b1dd9723df6cef0a66def3e
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dynamic-policy-evaluation-and-transparency-in-abac
    - Transparency in ABAC and Dynamic Policy Evaluation
    - DPEATIA
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: Dynamic Policy Evaluation and Transparency in ABAC
description: ABAC policies evaluate at query time based on user identity, group memberships, and object tags; tools like SHOW EFFECTIVE POLICIES help data consumers understand which rules apply to a given table.
tags:
  - abac
  - query-runtime
  - transparency
timestamp: "2026-06-19T09:09:13.895Z"
---

---
title: Dynamic Policy Evaluation and Transparency in ABAC
summary: ABAC policies are evaluated at query time based on the caller’s identity and the tags on the data object, which can make it harder for users to understand which access rules apply. Transparency requires deliberate documentation and tooling.
sources:
  - best-practices-for-abac-policies-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:45:52.790Z"
updatedAt: "2026-06-18T14:45:52.790Z"
tags:
  - databricks
  - abac
  - policy-evaluation
  - transparency
aliases:
  - dynamic-policy-evaluation-and-transparency-in-abac
  - DPETA
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Dynamic Policy Evaluation and Transparency in ABAC

**Dynamic Policy Evaluation and Transparency in ABAC** refers to the characteristic that [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies are resolved at query time, not pre‑attached to the table definition like traditional row filters or column masks. Because the effective rule depends on the user’s identity, group memberships, and the current tags on the data object, it can be difficult for data consumers and table owners to determine exactly which access restrictions apply to a given table without additional tooling. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## How Dynamic Evaluation Works

Unlike table-level row filters and column masks, which are directly visible on the table definition, ABAC policies are evaluated dynamically at query time. The evaluation uses:

- The caller’s identity and group memberships.
- The tags present on the data object (catalog, schema, table, or column) within the policy’s scope.
- The policy’s `MATCH COLUMNS`, `WHEN`, `TO`, and `EXCEPT` clauses.

This means the same table may present different data to different users, and a table owner cannot easily see all the policies that apply without running a specific command. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Recommended Practices for Transparency

To address the opacity of dynamic policy evaluation, the following practices are recommended:

1. **Use `SHOW EFFECTIVE POLICIES`** – Databricks provides the [`SHOW EFFECTIVE POLICIES`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-aux-show-policies) command to determine which ABAC policies apply to a specific table. This is the primary tool for understanding the effective governance on a given object. ^[best-practices-for-abac-policies-databricks-on-aws.md]

2. **Document the governance model** – Maintain clear documentation of the tagging taxonomy, all ABAC policies, and group management. Teams can then understand the governance model without inspecting every policy individually. ^[best-practices-for-abac-policies-databricks-on-aws.md]

3. **Consider table-level controls for high‑transparency tables** – If maximum transparency is critical for a specific table (for example, a shared reference table where any masking or filtering would be surprising), consider using [Row Filters and Column Masks (table-level)](/concepts/row-filters-and-column-masks.md) instead of ABAC policies. Those are directly visible on the table definition. However, possible conflicts between ABAC policies and table-level controls must be addressed first. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Why Transparency Matters

Dynamic evaluation makes ABAC powerful and scalable—policies automatically apply to new tables with matching tags—but it also creates a discoverability problem. Data consumers may not realize that a policy is filtering or masking their query results. Table owners may not know that a policy scoped at the catalog or schema level affects their table. Proactive documentation and tooling mitigate these risks. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related Concepts

- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) – Dynamic column masking based on tags.
- [ABAC Row Filter Policies](/concepts/abac-row-filter-policies.md) – Dynamic row filtering based on tags.
- Policy Evaluation Order – How multiple ABAC policies combine.
- [Governed Tags](/concepts/governed-tags.md) – The attributes driving policy conditions.
- [Row Filters and Column Masks (table-level)](/concepts/row-filters-and-column-masks.md) – Static, directly visible alternative.
- Best Practices for ABAC Policies – Broader guidance on policy design.

## Sources

- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)

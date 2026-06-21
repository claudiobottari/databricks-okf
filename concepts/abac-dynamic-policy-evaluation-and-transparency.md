---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 58c39501ac1d2a743fc1ca0cb8403c320b9f76ada56cb0b81c43ff1e1c827afa
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-dynamic-policy-evaluation-and-transparency
    - Transparency and ABAC Dynamic Policy Evaluation
    - ADPEAT
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: ABAC Dynamic Policy Evaluation and Transparency
description: The query-time nature of ABAC policy evaluation and practices to improve visibility for data consumers and table owners
tags:
  - abac
  - policy-evaluation
  - unity-catalog
  - transparency
timestamp: "2026-06-19T14:09:14.483Z"
---

# ABAC Dynamic Policy Evaluation and Transparency

**ABAC Dynamic Policy Evaluation and Transparency** refers to the nature of Attribute-Based Access Control (ABAC) policies in [Unity Catalog](/concepts/unity-catalog.md): they are evaluated at query time and are not directly visible on table definitions. This dynamic evaluation can create transparency challenges for data consumers and table owners, who may find it difficult to understand which access rules apply to a given table.

## Overview

ABAC policies differ from table-level row filters and column masks, which are directly visible on the table definition. Instead, ABAC policies evaluate at query time based on the user's identity, group memberships, and the tags on the data object in the policy scope. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Key Characteristics

- **Query-time evaluation**: ABAC policies are not stored as part of the table schema. Access decisions are recomputed on each query, considering the current user and current tag values.
- **User and group dependency**: The same table may yield different access rights for different users, depending on their group memberships.
- **Tag dependency**: Changes to object tags (e.g., from `public` to `confidential`) alter which policies apply without requiring table modification.

## Transparency Challenges

The dynamic nature of ABAC makes it harder for data consumers and table owners to understand which access rules apply to a specific table. Unlike static row filters or column masks, there is no single definition to inspect. This can lead to confusion during data exploration, troubleshooting, or access audits. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Mitigations

To improve transparency, the following practices are recommended:

1. **Use `SHOW EFFECTIVE POLICIES`** – Execute the [`SHOW EFFECTIVE POLICIES`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-aux-show-policies) command to determine what policies apply to a specific table for the current user. ^[best-practices-for-abac-policies-databricks-on-aws.md]

2. **Document the governance model** – Document the tagging taxonomy, policies, and group management approach so that teams can understand the governance model without inspecting each policy individually. ^[best-practices-for-abac-policies-databricks-on-aws.md]

3. **Consider table-level row filters or column masks for critical tables** – If transparency is essential for a specific table, fall back to [Row Filters](/concepts/row-filter-policies.md) or Column Masks attached directly to that table. These are directly visible in the table definition and offer static, transparent access rules. Ensure that any potential conflicts with ABAC policies are addressed first. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related Concepts

- [ABAC Policies in Unity Catalog](/concepts/abac-policies-in-unity-catalog.md) – The policy framework that provides dynamic, attribute-based access control.
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) – Static, table‑level access rules that are directly visible on the table definition.
- Tag Governance – Controls for standardising and auditing tags to support ABAC policies.
- [SHOW EFFECTIVE POLICIES](/concepts/show-effective-policies.md) – SQL command to inspect which policies apply to a table.
- [Unity Catalog Access Control](/concepts/unity-catalog-access-control-models.md) – Overall model for data governance in Databricks.

## Sources

- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)

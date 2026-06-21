---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c2c9f1b2fa80bff7f60befe8832c2703a9d927903b61ba282374f416d9826341
  pageDirectory: concepts
  sources:
    - requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multiple-abac-policy-resolution-rules
    - MAPRR
  citations:
    - file: requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
title: Multiple ABAC Policy Resolution Rules
description: Only one distinct row filter or column mask can resolve per user per table or column at runtime, otherwise Databricks blocks access
tags:
  - access-control
  - unity-catalog
  - policy-evaluation
  - databricks
timestamp: "2026-06-19T20:14:09.690Z"
---

# Multiple ABAC Policy Resolution Rules

**Multiple ABAC Policy Resolution Rules** define how Unity Catalog evaluates and applies attribute-based access control (ABAC) policies when multiple policies exist for the same table or column. These rules determine which policy takes effect at query time and prevent conflicts that could block access.

## Core Resolution Rule

When a user queries a table, only **one distinct row filter** and **one distinct column mask** can resolve at runtime for that user. If multiple distinct row filters or column masks apply to the same user and table or column, Databricks blocks access and returns an error. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Allowed Multiple Policies

Multiple ABAC policies are permitted if they resolve to the **same** row filter or column mask UDF with the same arguments. In this case, no conflict occurs because the policies produce identical filtering or masking behavior. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Conflict Detection

The system detects conflicts when two or more distinct policies would apply to the same user and the same table or column. Distinct policies means they have different UDF implementations or different arguments. When a conflict is detected, Databricks returns an error to the querying user rather than silently applying one policy over another. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- [ABAC Policy Evaluation](/concepts/dynamic-abac-policy-evaluation.md) – Detailed rules for how policies are evaluated at runtime
- [Row Filter Policies](/concepts/row-filter-policies.md) – Policies that restrict which rows a user can see
- [Column Mask Policies](/concepts/column-mask-policies.md) – Policies that modify or hide column values
- [Table-Level Row Filters and Column Masks](/concepts/table-level-row-filters-and-column-masks.md) – Non-ABAC filters and masks that can coexist with ABAC policies
- ABAC Limitations – Broader constraints on ABAC policy usage

## Sources

- requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws-43ef91f3.md)

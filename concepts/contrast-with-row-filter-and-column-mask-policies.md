---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bd731cca27d73b4fef50dc0646b06407e08c461f43be917e07a749cc4ebc0fdf
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - contrast-with-row-filter-and-column-mask-policies
    - Column Mask Policies and Contrast with Row Filter
    - CWRFACMP
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: Contrast with Row Filter and Column Mask Policies
description: "GRANT policies differ from row filter/column mask policies: they determine whether a user can access an object at all (vs restricting content), and they use inline conditions (vs requiring a UDF)."
tags:
  - access-control
  - unity-catalog
  - comparison
timestamp: "2026-06-18T14:15:54.394Z"
---

# Contrast with Row Filter and Column Mask Policies

**ABAC GRANT policies** differ from **row filter** and **column mask policies** in two fundamental ways: the type of access they control and the implementation mechanism they use. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Purpose: Access vs. Content

Row filter and column mask policies **restrict the content of data that a user can already access**. They operate *after* a user has been granted read privileges on a table, filtering which rows are visible or masking specific column values. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

GRANT policies, in contrast, **determine whether the user can access the object at all**. They control the initial grant of a privilege (such as `EXECUTE` on a model) based on tags, rather than restricting the data within an already-accessible object. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Implementation: UDF vs. Inline Condition

Row filter and column mask policies require a **user-defined function (UDF)** to implement the filter or mask logic. The UDF is created separately and then referenced by the policy. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

GRANT policies do not use UDFs. Instead, the condition that determines which objects the policy applies to is expressed **inline** in the policy definition, using built-in functions such as `has_tag_value`. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Summary Table

| Aspect | Row Filter / Column Mask Policies | GRANT Policies |
|--------|-----------------------------------|----------------|
| Control | Restrict content of already-accessed data | Determine whether access is granted at all |
| Implementation | Requires a user-defined function (UDF) | Condition expressed inline in policy definition |
| Typical use | Filter rows or mask columns in a table | Dynamically grant a privilege (e.g., `EXECUTE` on models) based on tags |

## Related Concepts

- [Row Filter Policies](/concepts/row-filter-policies.md) – ABAC policies that restrict visible rows in a table
- [Column Mask Policies](/concepts/column-mask-policies.md) – ABAC policies that mask sensitive column data
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) – The policy type that this page contrasts
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer supporting all three policy types

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)

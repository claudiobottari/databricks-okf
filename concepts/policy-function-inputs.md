---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b560db286b52c882135950815adccba5c3c59c2a587d7f91c0d1f93543452822
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - policy-function-inputs
    - PFI
    - Policy Function UDFs
  citations:
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: Policy Function Inputs
description: Parameters provided to row filter or column mask UDFs, which can be column values matched by tags, columns matched by custom expressions, or constant values.
tags:
  - unity-catalog
  - abac
  - udf
timestamp: "2026-06-19T18:00:06.528Z"
---

# Policy Function Inputs

**Policy Function Inputs** are the values supplied to the user-defined function (UDF) that implements the filtering or masking logic of an ABAC [row filter or column mask policy](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/policies) in Unity Catalog. When creating or editing a policy, you must specify a value for each parameter of the function that enforces the access control. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Input Types

Each function input can be one of three types: ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

1. **A column matched by tags** – The input is derived from a column that matches one of the governed tags defined in the policy's conditions.
2. **A column matched by a custom expression** – The input is derived from a column identified by a boolean expression using `has_tag` and `has_tag_value`, combined with `AND`, `OR`, and `NOT`.
3. **A constant value** – A fixed value provided directly. For example, a masking function parameter that specifies the number of characters to show (e.g., showing the last 4 characters of a Social Security number). ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Application to Row Filters

For [row filter policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/policies), the **Function inputs** section requires a value for each parameter of the row filter UDF. The UDF evaluates each row and returns a boolean; rows where the function returns `FALSE` are excluded from query results. Each input maps a column or constant value to a function parameter. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Application to Column Masks

For [column mask policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/policies), after specifying the columns to mask and selecting or creating a masking function, the **Function inputs** section provides a value for each additional function parameter (beyond the masked column itself). These inputs can also be columns matched by tags, columns matched by custom expressions, or constant values. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

For example, a masking function that redacts all but the last N characters of a column would have a constant input of `4` to indicate that the last 4 characters should be visible. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Configuration in Catalog Explorer

When creating a policy in the Catalog Explorer UI, the **Function inputs** section appears after selecting the policy type (row filter or column mask) and choosing or creating the function. Each field corresponds to a function parameter, and you select whether the input comes from a tag-matched column, a custom expression, or a constant value. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- [Row Filter Policies](/concepts/row-filter-policies.md)
- [Column Mask Policies](/concepts/column-mask-policies.md)
- ABAC Policy Core Concepts
- User-Defined Functions (UDFs) in Unity Catalog
- [Governed Tags](/concepts/governed-tags.md)
- Policy Function UDFs

## Sources

- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)

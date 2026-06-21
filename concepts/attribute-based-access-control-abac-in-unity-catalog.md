---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 296d81957138c437eee2a66d236a8addd443e182b49af6c47a5fe6de8ca140ad
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
    - attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
    - get-started-with-unity-catalog-databricks-on-aws.md
    - tutorial-configure-abac-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - attribute-based-access-control-abac-in-unity-catalog
    - AAC(IUC
    - Attribute-Based Access Control (ABAC) – Unity Catalog
    - Attribute-based access control (ABAC) with Unity Catalog
    - Attribute-based access control in Unity Catalog
    - attribute-based access control in Unity Catalog
  citations:
    - file: attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
    - file: tutorial-configure-abac-databricks-on-aws.md
title: Attribute-Based Access Control (ABAC) in Unity Catalog
description: Tag-driven centralized policies that dynamically filter and mask data across catalogs, recommended over per-table filters for scaling access control.
tags:
  - unity-catalog
  - access-control
  - abac
timestamp: "2026-06-19T21:55:11.706Z"
---



# Attribute-Based Access Control (ABAC) in Unity Catalog

**Attribute-based access control (ABAC)** is an access control model in [Unity Catalog](/concepts/unity-catalog.md) where access is determined by evaluating **attributes** (governed tags) associated with securable objects. These attributes are used in **policy** conditions to identify which data a policy should protect. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

Policies are attached at a level in the Unity Catalog hierarchy (such as a catalog, schema, or table) and are evaluated dynamically. When a securable object has the attributes targeted by a policy, that policy takes effect automatically, so a single policy can enforce consistent access rules across an entire catalog or schema. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Policy types

ABAC supports three types of policies:

- **[Row Filter Policies](/concepts/row-filter-policies.md)**: Hide entire rows from a query result based on a condition applied to a UDF. The UDF returns `TRUE` to show a row or `FALSE` to hide it. ^[tutorial-configure-abac-databricks-on-aws.md]
- **[Column Mask Policies](/concepts/column-mask-policies.md)**: Mask the data in a column (e.g., replace SSNs with `***-**-****`) based on a condition applied to a UDF. ^[tutorial-configure-abac-databricks-on-aws.md]
- **[ABAC GRANT Policy](/concepts/abac-grant-policy.md) (Beta)**: Dynamically grants a privilege (currently `EXECUTE` on models) to securable objects whose governed tags match a condition. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

Row filter and column mask policies are used on tables, materialized views, and streaming tables. GRANT policies are currently scoped to `EXECUTE` on models. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## How ABAC policies work

ABAC policies rely on governed tags that are assigned to columns or securable objects. For example, a tag key `pii` with allowed values `ssn` and `address` can be set on the `SSN` column and the `Address` column of a customer table. A column mask policy can then use the condition `has_tag_value('pii', 'ssn')` to trigger a UDF that masks the SSN value. ^[tutorial-configure-abac-databricks-on-aws.md]

Policies are created using SQL or the Catalog Explorer UI. They are attached to a catalog or schema (and, for row/column policies, can be applied to specific tables or columns). Principals are specified in the `TO` clause (and optionally `EXCEPT`) to control who is affected by the policy. ^[tutorial-configure-abac-databricks-on-aws.md]

When a user queries a table, Unity Catalog evaluates all applicable policies dynamically. The policy's UDF is invoked for each row or column; the returned value determines whether the row is shown or the column is masked. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Prerequisites

To use ABAC in Unity Catalog, you need:

- Databricks Runtime 16.4 or above, or serverless compute. (Older runtimes cannot access tables secured by ABAC.)
- Account admin or workspace admin permissions (to create governed tags).
- `MANAGE` permission on the target catalog or schema.
- `EXECUTE` permission on the UDFs used in the policies.

^[tutorial-configure-abac-databricks-on-aws.md]

## Creating a governed tag

Governed tags are created at the account level by account admins or workspace admins. In the Catalog Explorer, navigate to **Govern > Governed Tags** and click **Create governed tag**. Specify a key and allowed values. Only these values can be assigned to this tag key. ^[tutorial-configure-abac-databricks-on-aws.md]

## Example: Row filter and column mask

The [Tutorial: Configure ABAC](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/tutorial) demonstrates a complete example. In it, a US analytics team must be prevented from viewing EU customer records (row filter) and from seeing SSNs (column mask). A UDF `is_not_eu_address` checks if the address contains EU-related substrings, and a row filter policy hides rows where the UDF returns `FALSE`. A UDF `mask_ssn` returns `'***-**-****'` for any input, and a column mask policy applies it to columns tagged with `pii = 'ssn'`. ^[tutorial-configure-abac-databricks-on-aws.md]

## Related concepts

- [Governed Tags](/concepts/governed-tags.md) – The attribute mechanism that drives ABAC policies.
- [Row Filter Policies](/concepts/row-filter-policies.md) – Hides rows based on a UDF condition.
- [Column Mask Policies](/concepts/column-mask-policies.md) – Masks column data based on a UDF condition.
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) – Dynamic privilege grants using tags (Beta).
- [Unity Catalog Permissions Model](/concepts/unity-catalog-permissions-model.md) – The underlying privilege model that ABAC extends.
- [User-defined functions (UDFs)](/concepts/abac-user-defined-functions-udfs.md) – Functions that implement the filter or mask logic.

## Sources

- attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
- tutorial-configure-abac-databricks-on-aws.md

# Citations

1. [attribute-based-access-control-in-unity-catalog-databricks-on-aws.md](/references/attribute-based-access-control-in-unity-catalog-databricks-on-aws-23c11bc2.md)
2. [tutorial-configure-abac-databricks-on-aws.md](/references/tutorial-configure-abac-databricks-on-aws-cbba5828.md)

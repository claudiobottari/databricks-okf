---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c71d0fc87808ebca3eff1b80fb9a38fef1c9b09fcc9f702277732b28acfccc04
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-column-mask-policies
    - ACMP
  citations:
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: ABAC Column Mask Policies
description: A Unity Catalog policy type that masks column values in query results using a UDF, applicable to columns matched by governed tags or custom expressions.
tags:
  - data-governance
  - unity-catalog
  - access-control
  - abac
timestamp: "2026-06-19T17:59:52.183Z"
---

---
title: ABAC Column Mask Policies
summary: Policies that control how column values are presented to users based on tag-identified columns, using a UDF to return original or masked values, with automatic binding of the masked column as the first UDF argument.
sources:
  - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:45:52.790Z"
updatedAt: "2026-06-19T09:26:26.618Z"
tags:
  - access-control
  - column-level-security
  - unity-catalog
aliases:
  - abac-column-mask-policies
  - ACMP
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# ABAC Column Mask Policies

**ABAC Column Mask Policies** are a type of [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policy in Unity Catalog that dynamically mask column values for users based on governed tag conditions. Instead of applying a mask per table, a single policy defined at a catalog, schema, or table scope can automatically mask columns across many tables by matching tag expressions. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Requirements

To create or manage a column mask policy, the environment must meet these prerequisites: ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

- Databricks Runtime 16.4 or above, or serverless compute.
- A user-defined function (UDF) in Unity Catalog that implements the masking logic (or a SQL function defined inline when creating the policy).
- [Governed Tags](/concepts/governed-tags.md) applied to the target columns.
- `MANAGE` permission on the securable object (catalog, schema, or table) where the policy is attached, or ownership of that object.
- `EXECUTE` privilege on the UDF that performs the masking.

## Creating a Column Mask Policy

You can create a column mask policy using the Catalog Explorer UI, the `CREATE POLICY` SQL statement, or the Databricks REST APIs, SDKs, and Terraform. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Using Catalog Explorer

1. In your Databricks workspace, click **Catalog**.
2. Select the object that determines the policy scope (catalog, schema, or table).
3. Click the **Policies** tab, then **New policy**.
4. Complete the **Policy identification** section (name, description).
5. In **Principals and scope**, specify the users, groups, or service principals subject to the policy, and optionally an `EXCEPT` clause to exempt certain principals.
6. For **Policy type**, choose **Column mask**.
7. In the **Column conditions** section, choose how to identify columns to mask:
   - **Columns matching any of these tags**: Provide a list of tag keys or key‑value pairs.
   - **Columns matching a custom expression**: Build a boolean expression using `has_tag` and `has_tag_value`, combined with `AND`, `OR`, and `NOT`.
8. In the **Masking function** section, select an existing UDF or create a new SQL function. The return type must be castable to the target column’s data type.
9. In the **Function inputs** section, provide values for additional UDF parameters. Each input can be a column matched by tags, a column matched by a custom expression, or a constant value.
10. Click **Create policy**.

### Using SQL

The `CREATE POLICY` statement allows you to define the policy declaratively. The exact syntax supports specifying the masking UDF, column conditions, principals, and scope (catalog, schema, or table). ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Editing a Policy

You can edit a policy via Catalog Explorer, SQL (`ALTER POLICY`), or the SDK. Modifiable fields include the description, principals, policy type, conditions, and function input mappings. The policy name and the securable object where the policy is applied cannot be changed after creation. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Deleting a Policy

To delete a column mask policy, use Catalog Explorer (select the policy and click **Delete policy**) or the `DROP POLICY` SQL statement. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Viewing Policies

- `SHOW POLICIES ON { CATALOG | SCHEMA | TABLE }` lists policies defined directly on the object. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- `SHOW EFFECTIVE POLICIES ON { CATALOG | SCHEMA | TABLE }` also includes policies inherited from parent scopes (e.g., catalog‑level policies that affect a table). Viewing effective policies for a table does not require permissions on the parent catalog or schema. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- `DESCRIBE POLICY policy_name ON { CATALOG | SCHEMA | TABLE }` shows details of a specific policy, including its name, securable object, principals, conditions, function name, and timestamps. This requires `MANAGE` on the target securable object or ownership. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Audit Logging

Databricks logs governed tag and ABAC policy operations in the audit log system table (`system.access.audit`). You can query events such as `createPolicy`, `deletePolicy`, `getPolicy`, `listPolicies`, and tag assignment/deletion actions. Example queries are provided in the source documentation. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- [ABAC Row Filter Policies](/concepts/abac-row-filter-policies.md)
- [ABAC GRANT Policies](/concepts/abac-grant-policies.md)
- [Governed Tags](/concepts/governed-tags.md)
- User-Defined Function (UDF)
- Policy Evaluation Order
- [Row Filters and Column Masks (table-level)](/concepts/row-filters-and-column-masks.md)

## Sources

- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)

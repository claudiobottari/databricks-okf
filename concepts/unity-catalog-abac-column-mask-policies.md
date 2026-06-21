---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: efcab07fdae01025635f06b5db4d01962af6c3190443aba6f922e726032cfd58
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-abac-column-mask-policies
    - UCACMP
  citations:
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: Unity Catalog ABAC Column Mask Policies
description: Attribute-based access control policies that mask column values by applying a UDF to matched columns, identified via governed tags or custom expressions using has_tag and has_tag_value.
tags:
  - data-governance
  - unity-catalog
  - abac
  - security
timestamp: "2026-06-18T11:20:07.108Z"
---

# Unity Catalog ABAC Column Mask Policies

**Unity Catalog ABAC Column Mask Policies** are attribute-based access control policies in Unity Catalog that dynamically mask sensitive data in query results by replacing column values with a transformation defined by a user-defined function (UDF), evaluated based on the user's identity, group memberships, and the governed tags on the target columns. Unlike table-level column masks applied directly to a table definition, ABAC column mask policies evaluate tags at query time and can be scoped to entire catalogs or schemas, making them a dynamic, scalable alternative to static column-level masking.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## How Column Mask Policies Work

A column mask policy defines a **masking function** (a UDF) that transforms the original column value and a **condition** that identifies which columns to mask. The policy is attached to a catalog, schema, or table and includes a `WHEN` condition that matches governed tags on columns. When a user queries a table, Unity Catalog checks each column's governed tags against the policy's condition; for every column where the condition matches, the masking function is applied to the returned value.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

Column mask policies use [Governed Tags](/concepts/governed-tags.md) to identify which columns to mask. The policy can match columns by:
- A list of specific tag keys or tag key-value pairs.
- A custom boolean expression using `has_tag` and `has_tag_value`, combined with `AND`, `OR`, and `NOT`.

### Relationship to Row Filter Policies

Both row filter and column mask policies are [ABAC](/concepts/abac-attribute-based-access-control.md) policies in Unity Catalog. They share the same management operations—create, edit, delete, show, describe—and both require `MANAGE` on the securable object or object ownership. However, they serve different purposes:

- **Row filter policies** exclude entire rows from query results based on a filter condition.
- **Column mask policies** transform the values of matched columns while keeping all rows intact.

Row filter and column mask policies require a user-defined function (UDF) to implement the filter or mask logic. GRANT policies (Beta) do not use UDFs; the condition is expressed inline in the policy definition.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Requirements

All policy operations (create, edit, delete, show, describe) require `MANAGE` on the securable object where the policy is attached (catalog, schema, or table) or ownership of that securable object. Creating a policy also requires:^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

- Databricks Runtime 16.4 or above, or serverless compute.
- A user-defined function (UDF) in Unity Catalog that the creator has `EXECUTE` permission on, or a SQL function defined inline when creating the policy.
- Governed tags already applied to the target columns. See [Governed Tags](/concepts/governed-tags.md) for tag configuration instructions.

## Creating a Column Mask Policy

You can create a column mask policy using the Catalog Explorer UI, the `CREATE POLICY` SQL statement, or the Databricks REST APIs, SDKs, and Terraform.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

To create a policy, you must have `MANAGE` on the securable object where the policy is attached (catalog, schema, or table) or own that securable object, and `EXECUTE` on the UDF that implements the masking logic.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Using Catalog Explorer

1. In your Databricks workspace, click **Catalog**.
2. Select the object that determines the policy scope — this can be a catalog, schema, or table.
3. Click the **Policies** tab.
4. Click **New policy**.
5. Complete the **Policy identification** section.
6. Complete the **Principals and scope** section.
7. For **Policy type**, choose **Column mask**.
8. In the **Column conditions** section, choose how to identify the columns to mask:
   - **Columns matching any of these tags**: Specify a list of tag keys or tag key-value pairs.
   - **Columns matching a custom expression**: Build a boolean expression using `has_tag` and `has_tag_value`, combined with `AND`, `OR`, and `NOT`.
9. Choose the **Masking function** to apply to the matched columns:
   - **Select existing**: Select a UDF already defined in Unity Catalog. You must have `EXECUTE` on the UDF.
   - **Create**: Define a SQL function to use as the column masking logic.
10. In the **Function inputs** section, provide a value for each additional function parameter. Each input can be a column matched by tags, a column matched by a custom expression, or a constant value.
11. Click **Create policy**.

### Using SQL

```sql
CREATE POLICY policy_name
ON { CATALOG | SCHEMA | TABLE } securable_name
[COMMENT 'description']
TO `principal` [, `principal` ...]
[EXCEPT `principal` [, `principal` ...]]
ROW FILTER [input1_name, input2_name, ...] -- For row filters
COLUMN MASK [input1_name, input2_name, ...] -- For column masks
WHEN condition_expression;
```

### Using Python SDK

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

w.policies.create(
    name="mask_ssn",
    on_securable_type="SCHEMA",
    on_securable_full_name="prod.customers",
    principals=["data_analysts"],
    policy_type="COLUMN_MASK",
    when_condition="has_tag_value('sensitivity', 'confidential')",
    masking_function="mask_ssn_udf",
    function_inputs=[
        {"name": "ssn_column", "type": "column", "value": "ssn"},
        {"name": "visible_chars", "type": "constant", "value": "4"}
    ]
)
```

## Editing a Column Mask Policy

### Using Catalog Explorer

1. In your Databricks workspace, click **Catalog**.
2. Select the object the policy is attached to.
3. Click the **Policies** tab.
4. Select the policy you want to edit.
5. Update any fields you want to change. You can modify the description, principals, policy type, conditions, and function input mappings.
6. Click **Update policy**.

The policy name and the securable object where the policy is applied cannot be edited.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Deleting a Column Mask Policy

### Using Catalog Explorer

1. In your Databricks workspace, click **Catalog**.
2. Select the object the policy is attached to.
3. Click the **Policies** tab.
4. Select the policy.
5. Click **Delete policy**.

## Showing and Describing Policies

### Using SHOW POLICIES

Use `SHOW POLICIES` to list the policies defined on a securable object. Use `SHOW EFFECTIVE POLICIES` to also include policies from parent scopes, such as catalog-level policies that affect a table.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
SHOW [EFFECTIVE] POLICIES ON { CATALOG | SCHEMA | TABLE } securable_name
```

The result includes policy name, policy type, and the catalog, schema, or table where each policy is defined. Viewing effective policies for a table does not require permissions on the parent catalog or schema, allowing a table admin to see the rules that apply without having read access to sibling tables' policies.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Using DESCRIBE POLICY

Use `DESCRIBE POLICY` to view the details of a specific policy. Requires `MANAGE` on the target securable object or object ownership.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
{ DESC | DESCRIBE } POLICY policy_name ON { CATALOG | SCHEMA | TABLE } securable_name
```

The result shows the policy's properties as key-value pairs, including name, securable object type, securable object name, principals, conditions, function name, and timestamps.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Audit Logging

Databricks logs governed tag and ABAC policy operations in the [audit log system table](/concepts/audit-log-system-table-requirements.md). Below are example queries for auditing column mask policy operations:^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
-- All tag assignment and deletion events from the audit log
SELECT
  event_time,
  action_name,
  user_identity.email AS actor,
  request_params.workspace_id,
  request_params.metastore_id,
  request_params.tag_assignment,
  response.status_code,
  source_ip_address
FROM system.access.audit
WHERE service_name = 'unityCatalog'
  AND action_name IN (
    'createEntityTagAssignment',
    'deleteEntityTagAssignment'
  )
ORDER BY event_time DESC;
```

```sql
-- All ABAC policy CRUD operations
SELECT
  event_time,
  action_name,
  user_identity.email AS actor,
  request_params.name AS policy_name,
  request_params.on_securable_type,
  request_params.on_securable_fullname,
  request_params.policy_info,
  response.status_code
FROM system.access.audit
WHERE service_name = 'unityCatalog'
  AND action_name IN ('createPolicy', 'deletePolicy', 'getPolicy', 'listPolicies')
ORDER BY event_time DESC;
```

## Best Practices

- **Attach policies at the highest applicable scope.** Catalog-scoped or schema-scoped policies are preferred over table-scoped policies. They evaluate against all tables in the scope and apply automatically when new tables are added, as long as their tags match the policy's conditions.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Standardize your tagging taxonomy.** A small, well-defined set of tags with controlled values is easier to manage than a proliferation of ad-hoc tags.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Prevent policy sprawl.** ABAC is designed to reduce the number of access control rules, not increase them. Start with broad policies and consolidate overlapping ones.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Use groups in `TO` and `EXCEPT`, not individual users.** Adding or removing users from a group named in a policy changes who the policy applies to, without editing the policy.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Audit direct grants and ABAC policies together.** A user's effective privileges on a data object are the union of both. Checking only one surface can hide unintended permissions.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Use fallback mechanisms for unclassified data.** Apply a default restrictive tag like `classification : unverified` to new objects until a data steward reviews them, and create a policy that restricts access to objects with the default tag.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — The access control model underlying column mask policies
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that provides ABAC capabilities
- [Governed Tags](/concepts/governed-tags.md) — Tags used to identify columns for masking
- [Row Filter Policies](/concepts/row-filter-policies.md) — Related ABAC policies that exclude rows rather than masking columns
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Dynamic privilege grants based on tag conditions (Beta)
- [ABAC Policy Scoping and Sprawl Prevention](/concepts/abac-policy-scoping-and-sprawl-prevention.md) — Best practices for managing policy proliferation
- [ABAC Tagging Taxonomy and Governance](/concepts/abac-tagging-taxonomy-and-governance.md) — Tagging standards and governance practices
- [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) — System table used to audit tag and policy changes

## Sources

- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)

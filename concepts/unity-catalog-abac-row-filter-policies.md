---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7f662c3889fdf93629b87b3301390954d3cbb66833f106488414f1b2c3c3d4e9
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-abac-row-filter-policies
    - UCARFP
    - Unity Catalog ABAC policies
  citations:
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: Unity Catalog ABAC Row Filter Policies
description: Attribute-based access control policies that filter rows from query results based on a user-defined function (UDF) returning boolean values, excluding rows where the function returns FALSE.
tags:
  - data-governance
  - unity-catalog
  - abac
  - security
timestamp: "2026-06-18T11:19:31.829Z"
---

# Unity Catalog ABAC Row Filter Policies

**Row filter policies** are an [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) mechanism in [Unity Catalog](/concepts/unity-catalog.md) that dynamically exclude rows from query results based on the calling principal's identity, group memberships, and governed tags on the table. A row filter policy applies a user-defined function (UDF) to each row; rows for which the function returns `FALSE` are filtered out. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Overview

Row filter policies allow you to implement fine-grained, attribute-based row-level security without modifying the underlying table or writing per-query `WHERE` clauses. The policy is attached to a scope — a catalog, schema, or table — and evaluates a UDF against each row at query time. The UDF receives columns (or constant values) as inputs and returns a boolean. Only rows where the UDF returns `TRUE` are visible to the principal. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

Policies can target specific principals using `TO` and `EXCEPT` clauses, or use dynamic conditions inside the UDF (e.g., `is_account_group_member()`). Row filter policies are complementary to [ABAC Column Mask Policies](/concepts/abac-column-mask-policy.md), which mask column values rather than filtering rows. Unlike [ABAC GRANT Policies](/concepts/abac-grant-policy.md) (Beta), row filter policies do not grant privileges — they restrict data that the user already has permission to access. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Requirements

Before creating a row filter policy, you must satisfy the following prerequisites: ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

- **Permission**: You must have `MANAGE` on the securable object (catalog, schema, or table) where the policy is attached, or own that object. You also need `EXECUTE` on the UDF that implements the row filter logic.
- **Compute**: Databricks Runtime 16.4 or above, or serverless compute. See [Compute Requirements for ABAC Policies](/concepts/abac-compute-requirements.md).
- **UDF**: A user-defined function in Unity Catalog, or a SQL function defined inline when creating the policy. The UDF must be written in SQL or Python and return a boolean.
- **Governed tags**: (Optional) If the policy uses tag-based matching (e.g., `has_tag_value`), the target objects must have [Governed Tags](/concepts/governed-tags.md) applied.

## Creating a Row Filter Policy

You can create a row filter policy using the Catalog Explorer UI, SQL, or the Python SDK. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Using Catalog Explorer

1. In your Databricks workspace, click **Catalog**.
2. Select the object that determines the policy scope (catalog, schema, or table).
3. Click the **Policies** tab, then **New policy**.
4. Under **Policy type**, select **Row filter**.
5. In the **Row filter function** section, choose an existing UDF or create a new SQL function inline.
6. In the **Principals and scope** section, define which users and groups the policy applies to (via `TO` and optionally `EXCEPT`).
7. In the **Function inputs** section, map each UDF parameter to a column (matched by tags or custom expression) or a constant value.
8. Click **Create policy**. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Using SQL

Use the [`CREATE POLICY`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-policy) statement. For example:

```sql
CREATE POLICY eu_customer_filter
ON SCHEMA prod.customers
TO analysts, data_scientists
EXCEPT contractors
ROW FILTER
USING (region = 'EU')
USING FUNCTION eu_row_filter(region_col);
```

(Note: The exact syntax may vary; refer to the SQL reference for the current DDL.) ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Using Python SDK

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
w.policies.create(
    name="eu_customer_filter",
    parent_securable_type="SCHEMA",
    parent_securable_name="prod.customers",
    policy_type="ROW_FILTER",
    filter_function="eu_row_filter",
    function_inputs=[...],
    ...
)
```

(Full parameter details are in the SDK documentation.) ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Editing a Row Filter Policy

You can modify the description, principals, policy type, conditions, and function input mappings. The policy name and the securable object where it is attached cannot be changed. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Using Catalog Explorer

1. Select the object the policy is attached to.
2. Click the **Policies** tab, select the policy, and click **Edit**.
3. Update any editable fields and click **Update policy**. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Using SQL

Use `ALTER POLICY` or `REPLACE POLICY` depending on the desired behavior. (See the SQL language manual.) ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Deleting a Row Filter Policy

Deleting a policy removes the row filter from all tables in its scope. Requires `MANAGE` on the securable object or ownership. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

- **Catalog Explorer**: Select the object, Policies tab, select the policy, click **Delete policy**.
- **SQL**: `DROP POLICY policy_name ON { CATALOG | SCHEMA | TABLE } securable_name`. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Viewing Policies

### Show Policies

List all policies defined directly on a securable object, or include inherited policies from parent scopes using `EFFECTIVE`. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
SHOW [EFFECTIVE] POLICIES ON { CATALOG | SCHEMA | TABLE } securable_name
```

Example:

```sql
SHOW EFFECTIVE POLICIES ON SCHEMA prod.customers;
```

The result includes the policy name, type, and the scope where it is defined. Viewing effective policies for a table does not require permissions on the parent catalog or schema. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Describe a Policy

View detailed properties of a specific policy. Requires `MANAGE` on the target securable object or ownership. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
{ DESC | DESCRIBE } POLICY policy_name ON { CATALOG | SCHEMA | TABLE } securable_name
```

Example:

```sql
DESCRIBE POLICY hide_eu_customers ON SCHEMA prod.customers;
```

The output shows the policy's properties as key-value pairs: name, securable type, securable name, principals, conditions, function name, and timestamps. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Audit Logging

Databricks logs all governed tag and ABAC policy operations in the audit log system table (`system.access.audit`). You can query for policy CRUD events: ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
SELECT event_time, action_name, user_identity.email AS actor, request_params.name AS policy_name
FROM system.access.audit
WHERE service_name = 'unityCatalog'
  AND action_name IN ('createPolicy', 'deletePolicy', 'getPolicy', 'listPolicies')
ORDER BY event_time DESC;
```

This includes both row filter and column mask policies. Tag assignment events are also logged under `createEntityTagAssignment` and `deleteEntityTagAssignment`. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- [ABAC Column Mask Policies](/concepts/abac-column-mask-policy.md) — Mask column values instead of filtering rows
- [ABAC GRANT Policies](/concepts/abac-grant-policy.md) — Dynamic privilege grants based on tags (Beta)
- [Governed Tags](/concepts/governed-tags.md) — Tags used in ABAC policy conditions
- [Row Filter and Column Mask Policy Evaluation](/concepts/row-filter-policies.md) — Runtime behavior
- Performance Considerations for ABAC Policies
- ABAC Tutorials — Step-by-step guides
- [Unity Catalog UDFs](/concepts/unity-catalog.md) — Creating user-defined functions for policies
- [Compute Requirements for ABAC Policies](/concepts/abac-compute-requirements.md)

## Sources

- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)

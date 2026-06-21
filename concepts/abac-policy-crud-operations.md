---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c32e7dfd299b3197bfaec135dea9392cd6247e2d9e03afb20b9e3df7da67e37d
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policy-crud-operations
    - APCO
  citations:
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: ABAC Policy CRUD Operations
description: Operations to create, edit, view (SHOW/DESCRIBE), and delete ABAC row filter and column mask policies in Unity Catalog using Catalog Explorer UI, SQL, Python SDK, REST APIs, SDKs, or Terraform.
tags:
  - data-governance
  - unity-catalog
  - operations
timestamp: "2026-06-19T09:34:16.706Z"
---

#ABAC Policy CRUD Operations

**ABAC Policy CRUD Operations** refers to the process of creating, reading, updating, and deleting [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) row filter and column mask policies in Unity Catalog. These policies govern data access at the row and column level using governed tags and user attributes. The operations described here apply specifically to ABAC row filter and column mask policies; GRANT policies (Beta) have separate management workflows. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Requirements

All policy operations (create, edit, delete, show, describe) require `MANAGE` permission on the securable object (catalog, schema, or table) where the policy is attached, or ownership of that object. Creating a policy also requires:

- Databricks Runtime 16.4 or above, or serverless compute.
- A user-defined function (UDF) in Unity Catalog for the filtering or masking logic, with `EXECUTE` privilege granted to the creator, or a SQL function defined inline when creating the policy.
- [Governed Tags](/concepts/governed-tags.md) applied to the target columns or tables. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Create a Policy

Policies can be created using the Catalog Explorer UI, the `CREATE POLICY` SQL statement, or the Databricks REST APIs, SDKs, and Terraform. To create a policy, you must have `MANAGE` on the securable object where the policy is attached (catalog, schema, or table) or own the securable object, and `EXECUTE` on the UDF that implements the filtering or masking logic. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Using Catalog Explorer

1. In your Databricks workspace, click **Catalog**.
2. Select the object that determines the policy scope (catalog, schema, or table).
3. Click the **Policies** tab.
4. Click **New policy**.
5. Complete the **Policy identification** section (name, description).
6. Complete the **Principals and scope** section (list of users/groups subject to the policy, with optional `EXCEPT` clause and table condition).
7. For **Policy type**, choose **Row filter** or **Column mask**.
8. Depending on the type, configure the filter/mask function and its inputs. For row filters, choose an existing UDF or create a new SQL function; for column masks, specify column conditions (matching tags or custom expressions) and a masking function.
9. Click **Create policy**. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Using SQL

Use the `CREATE POLICY` SQL statement. Full syntax is documented in the [SQL language manual](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-policy). ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## View Policies

### List Policies

Use `SHOW POLICIES` to list the policies defined directly on a securable object. Use `SHOW EFFECTIVE POLICIES` to also include policies inherited from parent scopes (e.g., catalog-level policies that apply to a table). The result includes policy name, policy type, and the catalog, schema, or table where each policy is defined. Viewing effective policies for a table does not require permissions on the parent catalog or schema, enabling a table admin to see all applicable rules without access to sibling tables. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
SHOW EFFECTIVE POLICIES ON SCHEMA prod.customers;
```

### Describe a Policy

Use `DESCRIBE POLICY` to view the full properties of a specific policy, including name, securable object type, principals, conditions, function name, and timestamps. Requires `MANAGE` on the target securable object or ownership. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
DESCRIBE POLICY hide_eu_customers ON SCHEMA prod.customers;
```

## Edit a Policy

Policies can be edited using Catalog Explorer, SQL `ALTER POLICY`, or Python SDK. Editable fields include: description, principals, policy type (though switching type may require reconfiguration), conditions, and function input mappings. The policy name and the securable object where it is applied cannot be changed. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

To edit via Catalog Explorer:

1. Navigate to the object the policy is attached to.
2. Click the **Policies** tab.
3. Select the policy.
4. Update any fields you want to change.
5. Click **Update policy**. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Delete a Policy

To delete a policy, use Catalog Explorer, `DROP POLICY` SQL, or Python SDK. Deleting a policy removes the access restriction it enforces on all tables within its scope. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

Via Catalog Explorer:

1. Select the object the policy is attached to.
2. Click the **Policies** tab.
3. Select the policy.
4. Click **Delete policy**. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Audit Logging

Databricks logs all governed tag and ABAC policy operations in the audit log system table. The following example queries show how to retrieve tag assignment events and policy CRUD actions: ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
-- All ABAC policy CRUD operations
SELECT  event_time, action_name, user_identity.email AS actor,
        request_params.name AS policy_name,
        request_params.on_securable_type,
        request_params.on_securable_fullname,
        request_params.policy_info, response.status_code
FROM system.access.audit
WHERE service_name = 'unityCatalog'
  AND action_name IN ('createPolicy', 'deletePolicy', 'getPolicy', 'listPolicies')
ORDER BY event_time DESC;
```

Relevant action names include `createEntityTagAssignment`, `deleteEntityTagAssignment` for tags, and `createPolicy`, `deletePolicy`, `getPolicy`, `listPolicies` for ABAC policies. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- [ABAC Column Mask Policies](/concepts/abac-column-mask-policy.md)
- [ABAC Row Filter Policies](/concepts/abac-row-filter-policy.md)
- [Governed Tags](/concepts/governed-tags.md)
- [Row Filters and Column Masks (table-level)](/concepts/row-filters-and-column-masks.md)
- Policy Evaluation Order
- [Unity Catalog User-Defined Functions](/concepts/abac-user-defined-functions-udfs.md)

## Sources

- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)

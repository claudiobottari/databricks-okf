---
title: Create and manage row filter and column mask policies | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/policies
ingestedAt: "2026-06-18T08:03:31.503Z"
---

This page describes how to create, edit, view, and delete ABAC row filter and column mask policies in Unity Catalog. To create and manage GRANT policies (Beta), see [ABAC GRANT policies for models (Beta)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/grant-policies). For an overview of policy concepts, see [Core concepts for ABAC](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/core-concepts).

## Requirements[​](#requirements "Direct link to requirements")

All policy operations (create, edit, delete, show, describe) require `MANAGE` on the securable object or object ownership. Creating a policy also requires:

*   Databricks Runtime 16.4 or above, or serverless compute. See [Compute requirements](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/requirements#compute-requirements).
*   For the filtering or masking logic, a user-defined function (UDF) in Unity Catalog that you have `EXECUTE` on, or a SQL function that you define inline when creating the policy.
*   Governed tags applied to target objects. See [Governed tags](https://docs.databricks.com/aws/en/admin/governed-tags/).

## Create a policy[​](#create-a-policy "Direct link to create-a-policy")

You can create a policy using the Catalog Explorer UI, the [`CREATE POLICY`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-policy) SQL statement, or the Databricks REST APIs, SDKs, and Terraform.

To create a policy, you must have `MANAGE` on the securable object where the policy is attached (catalog, schema, or table) or own the securable object, and `EXECUTE` on the UDF that implements the filtering or masking logic.

*   Catalog Explorer
*   SQL
*   Python SDK

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
    
2.  Select the object that determines the policy scope, such as a catalog, schema, or table.
    
3.  Click the **Policies** tab.
    
4.  Click **New policy**.
    
5.  Complete the **Policy identification** section. The following table summarizes each field:
    
6.  Complete the **Principals and scope** section. The following table summarizes each field:
    
    ![Example ABAC policy settings for the Principals and scope section.](https://docs.databricks.com/aws/en/assets/images/abac-ui-principals-and-scope-a4af88618e1306ded74701ebec04d6a3.png)
    
7.  For **Policy type**, choose the type of access control to enforce:
    
8.  The next few sections depend on your **Policy type** selection. Expand the section that matches your selection:
    
    Row filter
    
    In the **Row filter function** section, choose how to specify the row filter function:
    
    *   **Select existing**: Select a UDF already defined in Unity Catalog. The UDF evaluates each row and returns a boolean. Rows where the function returns `FALSE` are excluded from query results. You must have `EXECUTE` on the UDF.
    *   **Create**: Define a SQL function to use as the row filter logic.
    
    ![Example ABAC row filter policy settings for the Row filter function section.](https://docs.databricks.com/aws/en/assets/images/abac-ui-row-filter-function-eu-c412f639a89b9a07c167475013b29606.png)
    
    In the **Function inputs** section, provide a value for each function parameter. Each input can be a column matched by tags, a column matched by a custom expression, or a constant value.
    
    ![Example ABAC settings for the Function inputs section.](https://docs.databricks.com/aws/en/assets/images/abac-ui-function-inputs-eu-21362a99c4bcbdaf8a063f8f147c08ab.png)
    
    Column mask
    
    In the **Column conditions** section, choose how to identify the columns to mask:
    
    *   **Columns matching any of these tags**: Specify a list of tag keys or tag key-value pairs. Columns that have any of these are masked by the policy.
    *   **Columns matching a custom expression**: Build a boolean expression using `has_tag` and `has_tag_value`, combined with `AND`, `OR`, and `NOT` for more complex matching logic. Columns where the expression evaluates to `TRUE` are masked.
    
    ![Example ABAC column mask policy settings for the Column conditions section.](https://docs.databricks.com/aws/en/assets/images/abac-ui-column-conditions-ssn-9fb549989ac6c78c37fa002c551fddd2.png)
    
    Then, choose the **Masking function** to apply to the matched columns:
    
    *   **Select existing**: Select a UDF already defined in Unity Catalog. The UDF returns the original or masked value. The return type must be castable to the target column's data type. You must have `EXECUTE` on the UDF.
    *   **Create**: Define a SQL function to use as the column masking logic.
    
    ![Example ABAC column mask policy settings for the Masking function section.](https://docs.databricks.com/aws/en/assets/images/abac-ui-masking-function-ssn-d923f031cca590b358bffb6b335a768a.png)
    
    In the **Function inputs** section, provide a value for each additional function parameter. Each input can be a column matched by tags, a column matched by a custom expression, or a constant value.
    
    This example uses a constant value of `4` to show the last 4 characters of the SSN.
    
    ![Example ABAC column mask policy settings for the Function inputs section.](https://docs.databricks.com/aws/en/assets/images/abac-ui-function-inputs-ssn-e9aa9c4f645d1e9b905c60854f68f50e.png)
    
9.  Click **Create policy**.
    

## Edit a policy[​](#edit-a-policy "Direct link to edit-a-policy")

*   Catalog Explorer
*   SQL
*   Python SDK

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
2.  Select the object the policy is attached to.
3.  Click the **Policies** tab.
4.  Select the policy you want to edit.
5.  Update any fields you want to change. You can modify the description, principals, policy type, conditions, and function input mappings. The policy name and the securable object where the policy is applied cannot be edited. For field descriptions, see [Create a policy](#create-policy).
6.  Click **Update policy**.

## Delete a policy[​](#delete-a-policy "Direct link to delete-a-policy")

*   Catalog Explorer
*   SQL
*   Python SDK

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
2.  Select the object the policy is attached to.
3.  Click the **Policies** tab.
4.  Select the policy.
5.  Click **Delete policy**.

## Show policies[​](#show-policies "Direct link to show-policies")

Use [`SHOW POLICIES`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-aux-show-policies) to list the policies defined on a securable object. Use `SHOW EFFECTIVE POLICIES` to also include policies from parent scopes, such as catalog-level policies that affect a table.

SQL

    SHOW [EFFECTIVE] POLICIES ON { CATALOG | SCHEMA | TABLE } securable_name

The result includes policy name, policy type, and the catalog, schema, or table where each policy is defined.

Viewing effective policies for a table does not require permissions on the parent catalog or schema. This allows a table admin to see the rules that apply without having read access to sibling tables' policies.

Example:

SQL

    SHOW EFFECTIVE POLICIES ON SCHEMA prod.customers;

## Describe a policy[​](#describe-a-policy "Direct link to describe-a-policy")

Use [`DESCRIBE POLICY`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-aux-describe-policy) to view the details of a specific policy. Requires `MANAGE` on the target securable object or object ownership.

SQL

    { DESC | DESCRIBE } POLICY policy_name ON { CATALOG | SCHEMA | TABLE } securable_name

The result shows the policy's properties as key-value pairs, including name, securable object type, securable object name, principals, conditions, function name, and timestamps.

Example:

SQL

    DESCRIBE POLICY hide_eu_customers ON SCHEMA prod.customers;

## Audit logging[​](#audit-logging "Direct link to audit-logging")

Databricks logs governed tag and ABAC policy operations in the audit log system table. Below are example queries. For more information, see [Audit logs](https://docs.databricks.com/aws/en/admin/system-tables/audit-logs).

SQL

    -- All tag assignment and deletion events from the audit logSELECT  event_time,  action_name,  user_identity.email AS actor,  request_params.workspace_id,  request_params.metastore_id,  request_params.tag_assignment,  response.status_code,  source_ip_addressFROM system.access.auditWHERE service_name = 'unityCatalog'  AND action_name IN (    'createEntityTagAssignment',    'deleteEntityTagAssignment'  )ORDER BY event_time DESC;-- All ABAC policy CRUD operationsSELECT  event_time,  action_name,  user_identity.email AS actor,  request_params.name AS policy_name,  request_params.on_securable_type,  request_params.on_securable_fullname,  request_params.policy_info,  response.status_codeFROM system.access.auditWHERE service_name = 'unityCatalog'  AND action_name IN ('createPolicy', 'deletePolicy', 'getPolicy', 'listPolicies')ORDER BY event_time DESC;

## More information[​](#more-information "Direct link to more-information")

*   [Core concepts for ABAC](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/core-concepts)
*   [Row filter and column mask policy evaluation and runtime behavior](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/policy-evaluation)
*   [Performance considerations for row filter and column mask policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/performance)
*   [ABAC tutorials](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/tutorial)
*   [Governed tags](https://docs.databricks.com/aws/en/admin/governed-tags/)
*   [Unity Catalog user-defined functions](https://docs.databricks.com/aws/en/udf/unity-catalog)

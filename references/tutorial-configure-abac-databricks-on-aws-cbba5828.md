---
title: "Tutorial: Configure ABAC | Databricks on AWS"
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/tutorial
ingestedAt: "2026-06-18T08:03:38.060Z"
---

This tutorial shows you how to configure row filter and column mask attribute-based access control (ABAC) policies in Unity Catalog using the Catalog Explorer UI. For a fully SQL-based version that also covers conditional email masking, see [Tutorial: Configure ABAC with SQL](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/tutorial-sql).

In this example, a US analytics team should not be able to access EU customer records or SSNs. However, they should be able to access other customers and customer data in the same table. This tutorial includes the following steps:

1.  Create a governed tag
2.  Create a Unity Catalog catalog, schema, and table
3.  Apply governed tags to columns
4.  Create a UDF for hiding EU member's data
5.  Create a row filter policy
6.  Create a UDF for hiding SSNs
7.  Create a column mask policy
8.  Select your table using the policies

For a demo of configuring ABAC, see [Discover Attribute-Based Access Control (ABAC) with Unity Catalog](https://app.getreprise.com/launch/G6Y2D0n/).

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

*   Databricks Runtime 16.4 or above, or serverless compute.
*   Account admin or workspace admin permissions (to create governed tags).
*   `MANAGE` permission on the target catalog or schema.
*   `EXECUTE` on the UDFs.

Compute running older runtimes cannot access tables secured by ABAC. As a temporary workaround, you can configure ABAC to apply only to a specific group. Add the users you want to restrict to that group. Users who are not in the group can still access the tables.

## Step 1: Create a governed tag[​](#step-1-create-a-governed-tag "Direct link to Step 1: Create a governed tag")

To create a governed tag, you must have the governed tag CREATE permission at the account level. Account and workspace admins have CREATE by default.

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
    
2.  Click the ![Shield icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0yIDEuNzVDMiAxLjMzNTc5IDIuMzM1NzkgMSAyLjc1IDFIMTMuMjVDMTMuNjY0MiAxIDE0IDEuMzM1NzkgMTQgMS43NVY5LjIxNDcyQzE0IDExLjIwNiAxMi45Njk3IDEzLjA1NTYgMTEuMjc2NSAxNC4xMDM3TDguMzk0NzcgMTUuODg3N0M4LjE1Mjg5IDE2LjAzNzQgNy44NDcxMSAxNi4wMzc0IDcuNjA1MjMgMTUuODg3N0w0LjcyMzQ2IDE0LjEwMzdDMy4wMzAzMSAxMy4wNTU2IDIgMTEuMjA2IDIgOS4yMTQ3MlYxLjc1Wk0zLjUgMi41VjdINy4yNVYyLjVIMy41Wk04Ljc1IDIuNVY3SDEyLjVWMi41SDguNzVaTTEyLjUgOC41SDguNzVWMTMuOTAzNkwxMC40ODcgMTIuODI4M0MxMS43Mzg1IDEyLjA1MzYgMTIuNSAxMC42ODY2IDEyLjUgOS4yMTQ3MlY4LjVaTTcuMjUgMTMuOTAzNlY4LjVIMy41VjkuMjE0NzJDMy41IDEwLjY4NjYgNC4yNjE1MyAxMi4wNTM2IDUuNTEyOTkgMTIuODI4M0w3LjI1IDEzLjkwMzZaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Govern** button.
    
3.  In the dropdown menu, click **Governed Tags**.
    
4.  Click **Create governed tag**.
    
5.  Enter the tag key `pii`.
    
6.  Enter a description for the governed tag.
    
7.  Enter the allowed values for the tag: `ssn` and `address`. Only these values can be assigned to this tag key.
    
    ![Tutorial: create a tag policy.](https://docs.databricks.com/aws/en/assets/images/create-tag-policy-abac-ab7467b3242c79c3e728b67c5f416df4.png)
    
8.  Click **Create**.
    

warning

Tag data is stored as plain text and may be replicated globally. Do not use tag names, values, or descriptors that could compromise the security of your resources. For example, do not use tag names, values or descriptors that contain personal or sensitive information.

## Step 2: Create the customers table[​](#step-2-create-the-customers-table "Direct link to Step 2: Create the customers table")

To follow these steps, you must have the `CREATE CATALOG` permission on your Unity Catalog metastore. You can also create the table in a schema that you have the `CREATE TABLE` permission on.

1.  In the sidebar, click **+New** > **Notebook**.
2.  Select `SQL` as your notebook language.
3.  Click **Connect** and attach the notebook to a compute resource.
4.  Add the following commands to the notebook and run them:

SQL

    -- Create catalog (if not already exists)CREATE CATALOG IF NOT EXISTS abac;USE CATALOG abac;-- Create schemaCREATE SCHEMA IF NOT EXISTS customers;USE SCHEMA customers;-- Create tableCREATE TABLE IF NOT EXISTS profiles (    First_Name STRING,    Last_Name STRING,    Phone_Number STRING,    Address STRING,    SSN STRING)USING DELTA;-- Insert dataINSERT INTO profiles (First_Name, Last_Name, Phone_Number, Address, SSN)VALUES('John', 'Doe', '123-456-7890', '123 Main St, NY', '123-45-6789'),('Jane', 'Smith', '234-567-8901', '456 Oak St, CA', '234-56-7890'),('Alice', 'Johnson', '345-678-9012', '789 Pine St, TX', '345-67-8901'),('Bob', 'Brown', '456-789-0123', '321 Maple St, FL', '456-78-9012'),('Charlie', 'Davis', '567-890-1234', '654 Cedar St, IL', '567-89-0123'),('Emily', 'White', '678-901-2345', '987 Birch St, WA', '678-90-1234'),('Frank', 'Miller', '789-012-3456', '741 Spruce St, WA', '789-01-2345'),('Grace', 'Wilson', '890-123-4567', '852 Elm St, NV', '890-12-3456'),('Hank', 'Moore', '901-234-5678', '963 Walnut St, CO', '901-23-4567'),('Ivy', 'Taylor', '012-345-6789', '159 Aspen St, AZ', '012-34-5678'),('Liam', 'Connor', '111-222-3333', '12 Abbey Street, Dublin, Ireland EU', '111-22-3333'),('Sophie', 'Dubois', '222-333-4444', '45 Rue de Rivoli, Paris, France Europe', '222-33-4444'),('Hans', 'Müller', '333-444-5555', '78 Berliner Str., Berlin, Germany E.U.', '333-44-5555'),('Elena', 'Rossi', '444-555-6666', '23 Via Roma, Milan, Italy Europe', '444-55-6666'),('Johan', 'Andersson', '555-666-7777', '56 Drottninggatan, Stockholm, Sweden EU', '555-66-7777');

1.  Add the following command to the notebook and run it:

SQL

    -- Add the governed tag to ssn columnALTER TABLE abac.customers.profilesALTER COLUMN SSNSET TAGS ('pii' = 'ssn');-- Add governed tag to address columnALTER TABLE abac.customers.profilesALTER COLUMN AddressSET TAGS ('pii' = 'address');

## Step 4: Create a UDF to find EU addresses[​](#step-4-create-a-udf-to-find-eu-addresses "Direct link to Step 4: Create a UDF to find EU addresses")

1.  Add the following command to the notebook and run it:

SQL

    -- Determine if an address is not in the EUCREATE OR REPLACE FUNCTION is_not_eu_address(address STRING)RETURNS BOOLEANRETURN (    SELECT CASE        WHEN LOWER(address) LIKE '%eu%'          OR LOWER(address) LIKE '%e.u.%'          OR LOWER(address) LIKE '%europe%'        THEN FALSE        ELSE TRUE    END);

This UDF checks whether a given string does not appear to reference Europe or the EU. If any of these substrings are found, it returns FALSE (meaning it is an EU address). If none of the substrings are found, it returns TRUE (meaning it is not an EU address).

## Step 5: Create a row filter policy[​](#step-5-create-a-row-filter-policy "Direct link to Step 5: Create a row filter policy")

To create a policy on an object, you must have `MANAGE` on the object or ownership of the object. To add a UDF to a policy, you must have `EXECUTE` on the UDF and it must be in Unity Catalog.

1.  Click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
    
2.  Click the `abac` catalog you created earlier.
    
3.  Click the **Policies** tab.
    
4.  Click **New policy**.
    
5.  In **General**:
    
    *   For **Name**, enter `hide_eu_customers`.
    *   For **Description**, enter a description for your policy.
    *   For **Applied to...**, search for and select the principals that the policy applies to. In this example, you can use the group **All account users**.
    *   Leave **Except for...** blank.
    *   For **Scope**, choose the `abac` catalog, and All schemas.
    
    ![Example ABAC row filter policy settings for the General section.](https://docs.databricks.com/aws/en/assets/images/abac-tutorial-rlf-general-71002d594bfe7e11b27e91ff6a71f90f.png)
    
6.  For **Purpose**, choose **Hide table rows**.
    
7.  In **Conditions**, click **Select existing**. Then, click ![Function icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzE2MDU1XzI4NzI3KSI+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNOS45MzA2NCAyLjk4ODE2QzkuMTU1NzEgMi4wODQwNyA3LjY3Nzc5IDIuNDk1ODYgNy40ODIwMyAzLjY3MDQyTDcuMDkzNzYgNi4wMDAwNkg5LjA5OTIyQzEwLjI1NTYgNi4wMDAwNiAxMS4yODg1IDYuNzIzNSAxMS42ODM3IDcuODEwMjdMMTEuNzU2OSA4LjAxMTU4TDEzLjk5MTQgNS45NDg5NkwxNS4wMDg4IDcuMDUxMTdMMTIuMzEyNiA5LjUzOTkzTDEyLjcyNjIgMTAuNjc3MkMxMi45MDU4IDExLjE3MTIgMTMuMzc1MyAxMS41MDAxIDEzLjkwMDkgMTEuNTAwMUgxNS4wMDAxVjEzLjAwMDFIMTMuOTAwOUMxMi43NDQ1IDEzLjAwMDEgMTEuNzExNyAxMi4yNzY2IDExLjMxNjUgMTEuMTg5OUwxMS4xMTc2IDEwLjY0M0w4LjUwODc5IDEzLjA1MTJMNy40OTEzNyAxMS45NDlMMTAuNTYxOSA5LjExNDY1TDEwLjI3NCA4LjMyMjg5QzEwLjA5NDMgNy44Mjg5IDkuNjI0ODYgNy41MDAwNiA5LjA5OTIyIDcuNTAwMDZINi44NDM3Nkw1Ljk5NzcyIDEyLjU3NjNDNS41OTI2MiAxNS4wMDY5IDIuNTM0MjYgMTUuODU5MSAwLjkzMDYzNiAxMy45ODgyTDIuMDY5NTIgMTMuMDEyQzIuODQ0NDUgMTMuOTE2MSA0LjMyMjM3IDEzLjUwNDMgNC41MTgxMyAxMi4zMjk3TDUuMzIzMDcgNy41MDAwNkgzLjAwMDA4VjYuMDAwMDZINS41NzMwN0w2LjAwMjQ0IDMuNDIzODJDNi40MDc1NCAwLjk5MzIzMyA5LjQ2NTkgMC4xNDEwNzcgMTEuMDY5NSAyLjAxMTk3TDkuOTMwNjQgMi45ODgxNloiIGZpbGw9IiM2RjZGNkYiLz4KPC9nPgo8ZGVmcz4KPGNsaXBQYXRoIGlkPSJjbGlwMF8xNjA1NV8yODcyNyI+CjxyZWN0IHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0id2hpdGUiIHRyYW5zZm9ybT0ibWF0cml4KC0xIDAgMCAxIDE2IDApIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==) **Select function**.
    
8.  In the **Select a function** menu, click the `abac` catalog, the `customers` schema, then the `is_not_eu_address` function you created earlier.
    
9.  Click **Select**.
    
    ![Example ABAC row filter policy settings for the Conditions section.](https://docs.databricks.com/aws/en/assets/images/abac-tutorial-rlf-conditions-c44e5c3ec7db2e0f572d675bd1cdd4f7.png)
    
10.  Optionally, you can test your masking function by expanding **Test function** and providing an input. For example, entering `78 Berliner Str., Berlin, Germany E.U.` and clicking **Run test** correctly returns `FALSE (Hide row)`.
     
     ![Example ABAC row filter masking function test.](https://docs.databricks.com/aws/en/assets/images/abac-tutorial-rlf-function-test-84a8112e5513677ffc659ce1a988ca11.png)
     
11.  In **Function parameters**:
     
     *   Choose **Map column to parameter if it has a specific tag**.
     *   Search for `pii`. Select `pii : address`.
     
     ![Example ABAC row filter policy settings for the Function parameters section.](https://docs.databricks.com/aws/en/assets/images/abac-tutorial-rlf-function-parameters-7a681bb5862f23b6f0a7058f3edd5943.png)
     
12.  Click **Create policy**.
     

## Step 6: Test your policy[​](#step-6-test-your-policy "Direct link to Step 6: Test your policy")

1.  Return to your notebook and run the following command:

SQL

    SELECT DISTINCT * FROM abac.customers.profiles

Only the non-EU resident rows are returned.

You can continue to create a column mask policy.

## Step 7: Create a UDF to mask SSNs[​](#step-7-create-a-udf-to-mask-ssns "Direct link to Step 7: Create a UDF to mask SSNs")

1.  Add the following command to the notebook and run it:

SQL

    -- Masks any SSN input by returning a fully masked valueCREATE FUNCTION mask_SSN(ssn STRING)RETURN '***-**-****' ;

This UDF returns a fully masked SSN string ('\*\*\*-\*\*-\*\*\*\*').

## Step 8: Create a column mask policy[​](#step-8-create-a-column-mask-policy "Direct link to Step 8: Create a column mask policy")

To create a policy on an object, you must have `MANAGE` on the object or ownership of the object. To add a UDF to a policy, you must have `EXECUTE` on the UDF and it must be in Unity Catalog.

1.  Click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
    
2.  Click the `abac` catalog you created earlier.
    
3.  Click the **Policies** tab.
    
4.  Click **New policy**.
    
5.  In **General**:
    
    *   For **Name**, enter `mask_ssn`.
    *   For **Description**, enter a description for your policy.
    *   For **Applied to...**, search for and select the principals that the policy applies to. In this example, you can use the group **All account users**.
    *   Leave **Except for...** blank.
    *   For **Scope**, choose the `abac` catalog, and All schemas.
    
    ![Example ABAC column mask policy settings for the General section.](https://docs.databricks.com/aws/en/assets/images/abac-tutorial-clm-general-acadef7fadad952495f926fe346dcaa5.png)
    
6.  For **Purpose**, choose **Mask column data**.
    
7.  In **Conditions**:
    
    *   Choose **Mask column if it has specific tag**. Search for `pii` and select `pii : ssn`.
    *   Click **Select existing**. Then, click ![Function icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzE2MDU1XzI4NzI3KSI+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNOS45MzA2NCAyLjk4ODE2QzkuMTU1NzEgMi4wODQwNyA3LjY3Nzc5IDIuNDk1ODYgNy40ODIwMyAzLjY3MDQyTDcuMDkzNzYgNi4wMDAwNkg5LjA5OTIyQzEwLjI1NTYgNi4wMDAwNiAxMS4yODg1IDYuNzIzNSAxMS42ODM3IDcuODEwMjdMMTEuNzU2OSA4LjAxMTU4TDEzLjk5MTQgNS45NDg5NkwxNS4wMDg4IDcuMDUxMTdMMTIuMzEyNiA5LjUzOTkzTDEyLjcyNjIgMTAuNjc3MkMxMi45MDU4IDExLjE3MTIgMTMuMzc1MyAxMS41MDAxIDEzLjkwMDkgMTEuNTAwMUgxNS4wMDAxVjEzLjAwMDFIMTMuOTAwOUMxMi43NDQ1IDEzLjAwMDEgMTEuNzExNyAxMi4yNzY2IDExLjMxNjUgMTEuMTg5OUwxMS4xMTc2IDEwLjY0M0w4LjUwODc5IDEzLjA1MTJMNy40OTEzNyAxMS45NDlMMTAuNTYxOSA5LjExNDY1TDEwLjI3NCA4LjMyMjg5QzEwLjA5NDMgNy44Mjg5IDkuNjI0ODYgNy41MDAwNiA5LjA5OTIyIDcuNTAwMDZINi44NDM3Nkw1Ljk5NzcyIDEyLjU3NjNDNS41OTI2MiAxNS4wMDY5IDIuNTM0MjYgMTUuODU5MSAwLjkzMDYzNiAxMy45ODgyTDIuMDY5NTIgMTMuMDEyQzIuODQ0NDUgMTMuOTE2MSA0LjMyMjM3IDEzLjUwNDMgNC41MTgxMyAxMi4zMjk3TDUuMzIzMDcgNy41MDAwNkgzLjAwMDA4VjYuMDAwMDZINS41NzMwN0w2LjAwMjQ0IDMuNDIzODJDNi40MDc1NCAwLjk5MzIzMyA5LjQ2NTkgMC4xNDEwNzcgMTEuMDY5NSAyLjAxMTk3TDkuOTMwNjQgMi45ODgxNloiIGZpbGw9IiM2RjZGNkYiLz4KPC9nPgo8ZGVmcz4KPGNsaXBQYXRoIGlkPSJjbGlwMF8xNjA1NV8yODcyNyI+CjxyZWN0IHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0id2hpdGUiIHRyYW5zZm9ybT0ibWF0cml4KC0xIDAgMCAxIDE2IDApIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==) **Select function**.
    *   In the **Select a function** menu, click the `abac` catalog, the `customers` schema, then the `mask_ssn` function you created earlier.
8.  Click **Select**.
    
    ![Example ABAC column mask policy settings for the Conditions section.](https://docs.databricks.com/aws/en/assets/images/abac-tutorial-clm-conditions-b399874fa0851a039706fac6d2001aad.png)
    
9.  Optionally, you can test your masking function by expanding **Test function** and providing an input. For example, entering `901-234-5678` and clicking **Run test** correctly returns `***-**-****`.
    
    ![Example ABAC column mask function test.](https://docs.databricks.com/aws/en/assets/images/abac-tutorial-clm-function-test-f539d320e2d5e986c397e2aadb58b893.png)
    
10.  Click **Create policy**.
     

## Step 9: Test your policy[​](#step-9-test-your-policy "Direct link to Step 9: Test your policy")

1.  Return to your notebook and run the following command:

SQL

    SELECT * FROM abac.customers.profiles

The SSNs now return as `***-**-****`. Only non-EU residents are returned because the row filter mask is also enabled.

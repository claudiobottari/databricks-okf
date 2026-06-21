---
title: "Tutorial: Configure ABAC with SQL | Databricks on AWS"
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/tutorial-sql
ingestedAt: "2026-06-18T08:03:39.686Z"
---

This tutorial shows you how to configure row filter and column mask ABAC policies in Unity Catalog using SQL. For the Catalog Explorer UI-based version, see [Tutorial: Configure ABAC](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/tutorial).

In this example, an analytics team cannot access EU customer records, and SSNs are always masked. Customers who have consented to data sharing have their full email shown. Others see a masked version only.

This tutorial includes the following steps:

1.  Create governed tags
2.  Create a Unity Catalog catalog, schema, and table
3.  Apply governed tags to columns
4.  Create a UDF to detect EU addresses
5.  Create a row filter policy
6.  Test the row filter
7.  Create a UDF to mask SSNs
8.  Create a column mask policy
9.  Test the column mask

After completing these steps, you can optionally extend the tutorial with conditional email masking (steps 10–12).

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

*   Databricks Runtime 16.4 or above, or serverless compute.
*   Account admin or workspace admin permissions (to create governed tags).
*   `MANAGE` permission on the target catalog or schema.
*   `EXECUTE` on the UDFs.

Compute running older runtimes cannot access tables secured by ABAC.

[Governed tags](https://docs.databricks.com/aws/en/admin/governed-tags/) are key-value pairs defined at the account level. ABAC policies use them to discover which columns to filter or mask. In this tutorial, you create two governed tags:

*   A `pii` tag with three allowed values: `ssn`, `address`, and `email`
*   A `consent` key-only tag (no allowed values) to identify consent columns

To create a governed tag, you must have the governed tag CREATE permission at the account level. Account and workspace admins have CREATE by default.

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
2.  Click the ![Shield icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0yIDEuNzVDMiAxLjMzNTc5IDIuMzM1NzkgMSAyLjc1IDFIMTMuMjVDMTMuNjY0MiAxIDE0IDEuMzM1NzkgMTQgMS43NVY5LjIxNDcyQzE0IDExLjIwNiAxMi45Njk3IDEzLjA1NTYgMTEuMjc2NSAxNC4xMDM3TDguMzk0NzcgMTUuODg3N0M4LjE1Mjg5IDE2LjAzNzQgNy44NDcxMSAxNi4wMzc0IDcuNjA1MjMgMTUuODg3N0w0LjcyMzQ2IDE0LjEwMzdDMy4wMzAzMSAxMy4wNTU2IDIgMTEuMjA2IDIgOS4yMTQ3MlYxLjc1Wk0zLjUgMi41VjdINy4yNVYyLjVIMy41Wk04Ljc1IDIuNVY3SDEyLjVWMi41SDguNzVaTTEyLjUgOC41SDguNzVWMTMuOTAzNkwxMC40ODcgMTIuODI4M0MxMS43Mzg1IDEyLjA1MzYgMTIuNSAxMC42ODY2IDEyLjUgOS4yMTQ3MlY4LjVaTTcuMjUgMTMuOTAzNlY4LjVIMy41VjkuMjE0NzJDMy41IDEwLjY4NjYgNC4yNjE1MyAxMi4wNTM2IDUuNTEyOTkgMTIuODI4M0w3LjI1IDEzLjkwMzZaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Govern** button.
3.  In the dropdown menu, click **Governed Tags**.
4.  Click **Create governed tag**.
5.  For the tag key, enter `pii`.
6.  Enter a description for the governed tag.
7.  For allowed values, enter: `ssn`, `address`, and `email`. Only these values can be assigned to this tag key.
8.  Click **Create**.
9.  Repeat steps 4–8 to create a second governed tag with the key `consent`. Leave the allowed values empty (key-only tag).

warning

Tag data is stored as plain text and may be replicated globally. Do not use tag names, values, or descriptors that could compromise the security of your resources. For example, do not use tag names, values or descriptors that contain personal or sensitive information.

## Step 2: Create the customers table[​](#step-2-create-the-customers-table "Direct link to Step 2: Create the customers table")

Create a catalog, schema, and table with customer profiles. The `has_consent` column is used later for conditional email masking. Customers who have given consent (`TRUE`) have their full email shown.

Run the following commands in a notebook attached to compute on Databricks Runtime 16.4 or above:

SQL

    -- Create catalog (if not already exists)CREATE CATALOG IF NOT EXISTS abac_tutorial;USE CATALOG abac_tutorial;-- Create schemaCREATE SCHEMA IF NOT EXISTS customers;USE SCHEMA customers;

SQL

    CREATE OR REPLACE TABLE profiles (    first_name STRING,    last_name STRING,    email STRING,    phone_number STRING,    home_address STRING,    ssn_number STRING,    has_consent BOOLEAN);

SQL

    INSERT INTO profiles (first_name, last_name, email, phone_number, home_address, ssn_number, has_consent)VALUES('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St, NY', '123-45-6789', TRUE),('Jane', 'Smith', 'jane.smith@example.com', '234-567-8901', '456 Oak St, CA', '234-56-7890', FALSE),('Alice', 'Johnson', 'alice.j@example.com', '345-678-9012', '789 Pine St, TX', '345-67-8901', TRUE),('Bob', 'Brown', 'bob.brown@example.com', '456-789-0123', '321 Maple St, FL', '456-78-9012', FALSE),('Charlie', 'Davis', 'charlie.d@example.com', '567-890-1234', '654 Cedar St, IL', '567-89-0123', TRUE),('Emily', 'White', 'emily.w@example.com', '678-901-2345', '987 Birch St, WA', '678-90-1234', FALSE),('Frank', 'Miller', 'frank.m@example.com', '789-012-3456', '741 Spruce St, WA', '789-01-2345', TRUE),('Grace', 'Wilson', 'grace.w@example.com', '890-123-4567', '852 Elm St, NV', '890-12-3456', TRUE),('Hank', 'Moore', 'hank.moore@example.com', '901-234-5678', '963 Walnut St, CO', '901-23-4567', FALSE),('Ivy', 'Taylor', 'ivy.taylor@example.com', '012-345-6789', '159 Aspen St, AZ', '012-34-5678', TRUE),('Liam', 'Connor', 'liam.c@example.com', '111-222-3333', '12 Abbey Street, Dublin, Ireland EU', '111-22-3333', TRUE),('Sophie', 'Dubois', 'sophie.d@example.com', '222-333-4444', '45 Rue de Rivoli, Paris, France Europe', '222-33-4444', FALSE),('Hans', 'Müller', 'hans.m@example.com', '333-444-5555', '78 Berliner Str., Berlin, Germany E.U.', '333-44-5555', TRUE),('Elena', 'Rossi', 'elena.r@example.com', '444-555-6666', '23 Via Roma, Milan, Italy Europe', '444-55-6666', FALSE),('Johan', 'Andersson', 'johan.a@example.com', '555-666-7777', '56 Drottninggatan, Stockholm, Sweden EU', '555-66-7777', TRUE);

Tag the `ssn_number`, `home_address`, and `email` columns with the `pii` governed tag. ABAC policies match columns by tag, not by name.

The `has_consent` column is tagged with the `consent` governed tag. This is required for the consent-aware masking policy in [Step 11](#step-11-create-the-conditional-email-masking-policy), which passes `has_consent` to the UDF via `USING COLUMNS`.

SQL

    ALTER TABLE abac_tutorial.customers.profilesALTER COLUMN ssn_numberSET TAGS ('pii' = 'ssn');ALTER TABLE abac_tutorial.customers.profilesALTER COLUMN home_addressSET TAGS ('pii' = 'address');ALTER TABLE abac_tutorial.customers.profilesALTER COLUMN emailSET TAGS ('pii' = 'email');ALTER TABLE abac_tutorial.customers.profilesALTER COLUMN has_consentSET TAGS ('consent' = '');

## Step 4: Create a UDF to detect EU addresses[​](#step-4-create-a-udf-to-detect-eu-addresses "Direct link to Step 4: Create a UDF to detect EU addresses")

This UDF is passed the value of every column tagged `pii = address` and returns:

*   `FALSE` if the address contains `EU`, `E.U.`, or `Europe` — the row is hidden.
*   `TRUE` otherwise — the row is shown.

SQL

    CREATE OR REPLACE FUNCTION is_not_eu_address(address STRING)RETURNS BOOLEANRETURN (    SELECT CASE        WHEN LOWER(address) LIKE '%eu%'          OR LOWER(address) LIKE '%e.u.%'          OR LOWER(address) LIKE '%europe%'        THEN FALSE        ELSE TRUE    END);

note

This is a simplified check for demonstration purposes. In production, use a more robust method such as a country code column or a lookup table to determine region.

## Step 5: Create a row filter policy[​](#step-5-create-a-row-filter-policy "Direct link to Step 5: Create a row filter policy")

To create a policy, you must have `MANAGE` on the object or ownership of the object. To add a UDF to a policy, you must have `EXECUTE` on the UDF.

SQL

    CREATE POLICY hide_eu_customersON SCHEMA abac_tutorial.customersROW FILTER is_not_eu_addressTO `account users`FOR TABLESMATCH COLUMNS has_tag_value('pii', 'address') AS addr_colUSING COLUMNS (addr_col);

You can also create policies through the Catalog Explorer UI. See [Create and manage row filter and column mask policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/policies) for details.

## Step 6: Test the row filter[​](#step-6-test-the-row-filter "Direct link to Step 6: Test the row filter")

Run the following query to verify that the row filter policy is working.

SQL

    SELECT * FROM abac_tutorial.customers.profiles;

Only the 10 non-EU resident rows are returned. The five EU customers (Liam, Sophie, Hans, Elena, and Johan) are hidden.

## Step 7: Create a UDF to mask SSNs[​](#step-7-create-a-udf-to-mask-ssns "Direct link to Step 7: Create a UDF to mask SSNs")

This UDF returns a fully-redacted placeholder for any SSN value passed to it.

SQL

    CREATE OR REPLACE FUNCTION redact_ssn(ssn STRING)RETURNS STRINGRETURN '***-**-****';

## Step 8: Create a column mask policy[​](#step-8-create-a-column-mask-policy "Direct link to Step 8: Create a column mask policy")

Create a policy that targets all columns tagged `pii = ssn` and applies the `redact_ssn` function to each.

SQL

    CREATE POLICY redact_ssn_policyON SCHEMA abac_tutorial.customersCOLUMN MASK redact_ssnTO `account users`FOR TABLESMATCH COLUMNS has_tag_value('pii', 'ssn') AS ssn_colON COLUMN ssn_col;

## Step 9: Test the column mask[​](#step-9-test-the-column-mask "Direct link to Step 9: Test the column mask")

Run the following query to verify that both the row filter and column mask are active.

SQL

    SELECT * FROM abac_tutorial.customers.profiles;

SSNs now return as `***-**-****`. Only non-EU residents are returned because the row filter is also active.

## Extend: Conditional email masking[​](#extend-conditional-email-masking "Direct link to Extend: Conditional email masking")

The following steps extend the tutorial with consent-aware email masking. Customers who opted in (`has_consent = TRUE`) have their full email shown; others see only the first character and domain.

### Step 10: Create a consent-aware email masking UDF[​](#step-10-create-a-consent-aware-email-masking-udf "Direct link to Step 10: Create a consent-aware email masking UDF")

This UDF takes two arguments:

*   `email`: the actual email value from the matched column
*   `consent`: the value of the `has_consent` column on the same row

SQL

    CREATE OR REPLACE FUNCTION mask_email_by_consent(email STRING, consent BOOLEAN)RETURNS STRINGRETURN CASE  WHEN consent = TRUE THEN email  ELSE CONCAT(LEFT(email, 1), '***@', SUBSTRING_INDEX(email, '@', -1))END;

### Step 11: Create the conditional email masking policy[​](#step-11-create-the-conditional-email-masking-policy "Direct link to Step 11: Create the conditional email masking policy")

This policy targets columns tagged `pii = email` and passes the `has_consent` column to the UDF.

note

The `has_consent` column was tagged with the `consent` governed tag in [Step 3](#step-3-add-governed-tags-to-columns). This is required because `USING COLUMNS` can only reference columns that are matched via `MATCH COLUMNS`. Even though `has_consent` is not being masked, it must be tagged so the policy can pass its value to the UDF.

SQL

    CREATE POLICY mask_email_by_consent_policyON SCHEMA abac_tutorial.customersCOLUMN MASK mask_email_by_consentTO `account users`FOR TABLESMATCH COLUMNS has_tag_value('pii', 'email') AS email_col,  has_tag('consent') AS consent_colON COLUMN email_colUSING COLUMNS (consent_col);

### Step 12: Test conditional email masking[​](#step-12-test-conditional-email-masking "Direct link to Step 12: Test conditional email masking")

Run the following query to verify that all three policies are working together.

SQL

    SELECT * FROM abac_tutorial.customers.profiles;

Customers with `has_consent = TRUE` have their full email shown. Customers with `has_consent = FALSE` see a masked version. SSNs remain fully masked, and only non-EU customers are returned.

## Summary[​](#summary "Direct link to Summary")

This tutorial demonstrated three ABAC patterns:

*   **Row filtering**: hide rows based on column values matched by governed tags
*   **Column masking**: mask columns matched by governed tags
*   **Conditional masking**: mask a column based on another column's value on the same row, by tagging the context column and passing it to the UDF via `USING COLUMNS`

## Clean up[​](#clean-up "Direct link to Clean up")

To remove all objects created in this tutorial, run the following. If you skipped the conditional email masking steps, the `DROP POLICY mask_email_by_consent_policy` and `DROP FUNCTION mask_email_by_consent` statements fail, which is expected.

SQL

    DROP POLICY hide_eu_customers ON SCHEMA abac_tutorial.customers;DROP POLICY redact_ssn_policy ON SCHEMA abac_tutorial.customers;DROP POLICY mask_email_by_consent_policy ON SCHEMA abac_tutorial.customers;DROP FUNCTION IF EXISTS abac_tutorial.customers.is_not_eu_address;DROP FUNCTION IF EXISTS abac_tutorial.customers.redact_ssn;DROP FUNCTION IF EXISTS abac_tutorial.customers.mask_email_by_consent;DROP TABLE IF EXISTS abac_tutorial.customers.profiles;DROP SCHEMA IF EXISTS abac_tutorial.customers CASCADE;

To remove the `pii` and `consent` governed tags, use the Catalog Explorer UI.

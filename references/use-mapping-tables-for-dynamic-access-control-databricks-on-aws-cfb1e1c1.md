---
title: Use mapping tables for dynamic access control | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/mapping-tables
ingestedAt: "2026-06-18T08:03:26.286Z"
---

This tutorial shows how to use a mapping table to control row-level and column-level access without managing a large number of groups. A single lookup table drives both row filtering and column masking. Access changes require only a row update. You don't need to create new groups or rewrite policies.

This tutorial also demonstrates conditional masking: PII columns are masked differently depending on the value of another column on the same row. Orders marked `confidential` have their PII fully redacted regardless of the user's clearance level.

For general guidance on mapping table design, see [Use mapping tables to create an access-control list](https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/manually-apply#use-mapping-tables-to-create-an-access-control-list).

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

*   Databricks Runtime 16.4 or above, or serverless compute.
*   Account admin or workspace admin permissions (to create governed tags).
*   `MANAGE` permission on the target catalog or schema.
*   `EXECUTE` on the UDFs.
*   A SQL notebook or query editor.

## Scenario[​](#scenario "Direct link to Scenario")

Your organization has employees across four regions (US East, US West, EU, APAC) and four departments. Each user should see only the rows that match their region and department, and PII columns should be masked based on two factors: the user's clearance level (`full`, `masked`, or `none`) stored in a mapping table, and the order's `order_priority`.

With a group-based approach, you need a group for every region-department combination. For example, you need 16 groups for four regions and four departments. Adding PII clearance tiers triples that count. Each new region or department requires new groups and policy updates.

The mapping table approach replaces this with a single lookup table: one row per user, one column per access dimension. To change a user's access, you update a row.

Before running any SQL, create the following governed tags in the Catalog Explorer UI (**Catalog** > **Govern** > **Governed Tags** > **Create governed tag**):

The `region` and `department` tags tell the row filter policy which columns to pass to the filter UDF. The `pii` tag tells the column mask policies which columns to mask and what PII type they contain. The `priority` tag lets the column mask policies pass the `order_priority` value to the mask UDF for conditional masking.

warning

Tag data is stored as plain text and may be replicated globally. Do not use tag names, values, or descriptors that could compromise the security of your resources. For example, do not use tag names, values or descriptors that contain personal or sensitive information.

## Step 2: Build sample data[​](#step-2-build-sample-data "Direct link to Step 2: Build sample data")

Create a catalog, schema, and orders table. The `order_priority` column drives conditional masking: orders marked `confidential` have their PII fully redacted, even for users with high clearance.

SQL

    CREATE CATALOG IF NOT EXISTS abac_tutorial;USE CATALOG abac_tutorial;CREATE SCHEMA IF NOT EXISTS mapping_demo;USE SCHEMA mapping_demo;

SQL

    CREATE OR REPLACE TABLE orders (  order_id INT,  customer_name STRING,  customer_email STRING,  sales_region STRING,  dept STRING,  amount DOUBLE,  order_date DATE,  order_priority STRING);INSERT INTO orders VALUES  (1,  'Acme Corp',     'orders@acme.com',    'us_east', 'engineering', 50000,  '2025-01-15', 'standard'),  (2,  'Beta Inc',      'sales@beta.com',     'us_east', 'sales',       75000,  '2025-02-01', 'confidential'),  (3,  'Gamma LLC',     'info@gamma.com',     'us_west', 'engineering', 30000,  '2025-01-20', 'standard'),  (4,  'Delta Co',      'deals@delta.com',    'us_west', 'sales',       95000,  '2025-03-01', 'confidential'),  (5,  'Epsilon GmbH',  'kontakt@epsilon.de', 'eu',      'engineering', 45000,  '2025-02-15', 'standard'),  (6,  'Zeta SA',       'contact@zeta.fr',    'eu',      'sales',       62000,  '2025-01-30', 'standard'),  (7,  'Eta Ltd',       'hello@eta.sg',       'apac',    'marketing',   28000,  '2025-03-10', 'confidential'),  (8,  'Theta Corp',    'biz@theta.com',      'us_east', 'marketing',   55000,  '2025-02-20', 'standard'),  (9,  'Iota KK',       'info@iota.jp',       'apac',    'engineering', 41000,  '2025-01-25', 'standard'),  (10, 'Kappa Inc',     'sales@kappa.com',    'us_west', 'marketing',   33000,  '2025-03-05', 'standard');

Tag the columns so that ABAC policies can discover them automatically. The `order_priority` column is tagged with the key-only `priority` tag so that the column mask policies can match it via `MATCH COLUMNS` and pass its value to the mask UDF.

SQL

    ALTER TABLE abac_tutorial.mapping_demo.orders  ALTER COLUMN sales_region SET TAGS ('region' = '');ALTER TABLE abac_tutorial.mapping_demo.orders  ALTER COLUMN dept SET TAGS ('department' = '');ALTER TABLE abac_tutorial.mapping_demo.orders  ALTER COLUMN customer_name SET TAGS ('pii' = 'name');ALTER TABLE abac_tutorial.mapping_demo.orders  ALTER COLUMN customer_email SET TAGS ('pii' = 'email');ALTER TABLE abac_tutorial.mapping_demo.orders  ALTER COLUMN order_priority SET TAGS ('priority' = '');

## Step 4: Create the mapping table[​](#step-4-create-the-mapping-table "Direct link to Step 4: Create the mapping table")

Instead of creating groups for every region, department, and clearance combination, you maintain one table with one row per user. The `pii_access` column controls how PII columns appear:

*   `full` — see the actual value (for standard-priority orders)
*   `masked` — see a partial value such as `A***` or `o***@acme.com`
*   `none` — see `***REDACTED***`

The `expires_on` column sets an expiration date for each access entry. After this date, the row filter UDF stops matching the entry and the user silently loses access with no manual revocation needed. This is useful for contractors, temporary data sharing agreements, or time-limited projects.

If a user needs access to multiple region and department combinations, add additional rows.

note

Keep mapping tables small and simple. Each query against a protected table runs the row filter and column mask UDFs, which in turn query the mapping table. Large mapping tables and complex UDF logic can impact query performance. Use narrow schemas and keep UDF logic to a single lookup where possible.

SQL

    CREATE OR REPLACE TABLE abac_tutorial.mapping_demo.user_access (  user_email STRING,  region STRING,  department STRING,  pii_access STRING,  expires_on DATE);INSERT INTO abac_tutorial.mapping_demo.user_access VALUES  (current_user(),      'us_east', 'engineering', 'masked', '2099-12-31'),  ('bob@example.com',   'us_west', 'sales',       'full',   '2099-12-31'),  ('carol@example.com', 'eu',      'engineering', 'none',   '2099-12-31'),  ('david@example.com', 'apac',    'marketing',   'masked', '2099-12-31');

## Step 5: Create the row filter UDF[​](#step-5-create-the-row-filter-udf "Direct link to Step 5: Create the row filter UDF")

This UDF receives a row's `sales_region` and `dept` values (passed in by the policy via tag matching), looks up the current user in the mapping table, and returns `TRUE` only if a matching entry exists and has not expired. Users not in the mapping table, or whose access has expired, see no rows ([fail-closed design](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/policy-evaluation#fail-closed)).

SQL

    CREATE OR REPLACE FUNCTION abac_tutorial.mapping_demo.access_filter(  region_val STRING,  dept_val STRING)RETURNS BOOLEANRETURN EXISTS (  SELECT 1 FROM abac_tutorial.mapping_demo.user_access  WHERE user_email = current_user()    AND region = region_val    AND department = dept_val    AND expires_on >= current_date());

## Step 6: Create the column mask UDF[​](#step-6-create-the-column-mask-udf "Direct link to Step 6: Create the column mask UDF")

This UDF controls how PII columns are displayed. It takes three arguments: the column value, the PII type (`'name'` or `'email'`), and the row's `order_priority`. The masking logic has two layers:

*   **Layer 1 (conditional masking):** If `order_priority` is `confidential`, the PII is always fully redacted regardless of the user's clearance level.
*   **Layer 2 (user clearance):** For standard rows, the UDF checks the mapping table for the user's `pii_access` level and applies the corresponding mask. If a user has multiple mapping table entries (multi-region access), the highest clearance across all rows applies.

SQL

    CREATE OR REPLACE FUNCTION abac_tutorial.mapping_demo.pii_mask(  val STRING,  pii_type STRING,  order_pri STRING)RETURNS STRINGRETURN CASE  WHEN order_pri = 'confidential' THEN '***REDACTED***'  WHEN EXISTS (    SELECT 1 FROM abac_tutorial.mapping_demo.user_access    WHERE user_email = current_user() AND pii_access = 'full'  ) THEN val  WHEN EXISTS (    SELECT 1 FROM abac_tutorial.mapping_demo.user_access    WHERE user_email = current_user() AND pii_access = 'masked'  ) THEN    CASE pii_type      WHEN 'email' THEN CONCAT(LEFT(val, 1), '***@', SUBSTRING_INDEX(val, '@', -1))      WHEN 'name'  THEN CONCAT(LEFT(val, 1), '***')      ELSE CONCAT(LEFT(val, 1), '***')    END  ELSE '***REDACTED***'END;

## Step 7: Create the policies[​](#step-7-create-the-policies "Direct link to Step 7: Create the policies")

Create three policies, all driven by the same mapping table. Both column mask policies use the same `pii_mask` function. The `pii_type` argument tells the function which masking style to apply, so you don't need a separate UDF per column type.

The `priority` governed tag is used in `MATCH COLUMNS` to match the `order_priority` column and pass its value to the mask UDF as `order_pri`. This is how conditional masking is implemented: the policy passes the row's priority value to the UDF at query time.

SQL

    CREATE POLICY user_access_filterON SCHEMA abac_tutorial.mapping_demoROW FILTER abac_tutorial.mapping_demo.access_filterTO `account users`FOR TABLESMATCH COLUMNS has_tag('region') AS r, has_tag('department') AS dUSING COLUMNS (r, d);

SQL

    CREATE POLICY pii_mask_nameON SCHEMA abac_tutorial.mapping_demoCOLUMN MASK abac_tutorial.mapping_demo.pii_maskTO `account users`FOR TABLESMATCH COLUMNS has_tag_value('pii', 'name') AS m,  has_tag('priority') AS priON COLUMN mUSING COLUMNS ('name', pri);CREATE POLICY pii_mask_emailON SCHEMA abac_tutorial.mapping_demoCOLUMN MASK abac_tutorial.mapping_demo.pii_maskTO `account users`FOR TABLESMATCH COLUMNS has_tag_value('pii', 'email') AS m,  has_tag('priority') AS priON COLUMN mUSING COLUMNS ('email', pri);

## Step 8: Verify the results[​](#step-8-verify-the-results "Direct link to Step 8: Verify the results")

Your mapping table entry gives you access to `us_east / engineering` with `masked` clearance. Run the following query to verify that you see only order #1, with PII partially masked.

SQL

    SELECT * FROM abac_tutorial.mapping_demo.orders;

Order #1 has `order_priority = 'standard'`, so your `masked` clearance applies.

**Expected result for your user:**

**What other users see:**

Notice that bob has `full` clearance but still sees `***REDACTED***` because order #4 is `confidential`. This is conditional masking: the row's priority value overrides user clearance.

## Step 9: Update access dynamically[​](#step-9-update-access-dynamically "Direct link to Step 9: Update access dynamically")

The key benefit of the mapping table approach is that you can change access by updating rows in the table. You don't need to update policies, UDFs, or group memberships.

### Reassign to a different department[​](#reassign-to-a-different-department "Direct link to Reassign to a different department")

Change your department from `engineering` to `sales`. Order #2 (Beta Inc) is a `confidential` sales order, so its PII is fully redacted even with `masked` clearance.

SQL

    UPDATE abac_tutorial.mapping_demo.user_accessSET department = 'sales'WHERE user_email = current_user();

Run the following query to verify. You should see order #2 with `***REDACTED***` PII.

SQL

    SELECT * FROM abac_tutorial.mapping_demo.orders;

Revert the change:

SQL

    UPDATE abac_tutorial.mapping_demo.user_accessSET department = 'engineering'WHERE user_email = current_user();

### Upgrade PII clearance[​](#upgrade-pii-clearance "Direct link to Upgrade PII clearance")

Change your clearance from `masked` to `full`. For standard-priority rows, you now see the actual PII values.

SQL

    UPDATE abac_tutorial.mapping_demo.user_accessSET pii_access = 'full'WHERE user_email = current_user();

Run the following query to verify. Order #1 is `standard` priority, so with `full` clearance you should see `Acme Corp` and `orders@acme.com`.

SQL

    SELECT * FROM abac_tutorial.mapping_demo.orders;

Revert the change:

SQL

    UPDATE abac_tutorial.mapping_demo.user_accessSET pii_access = 'masked'WHERE user_email = current_user();

### Grant access to an additional region[​](#grant-access-to-an-additional-region "Direct link to Grant access to an additional region")

Insert a second row to grant access to EU engineering. No new groups or policies are required.

SQL

    INSERT INTO abac_tutorial.mapping_demo.user_accessVALUES (current_user(), 'eu', 'engineering', 'masked', '2099-12-31');

Run the following query to verify. You should now see both order #1 (us\_east, engineering) and order #5 (eu, engineering), with PII partially masked.

SQL

    SELECT * FROM abac_tutorial.mapping_demo.orders;

Remove the additional access:

SQL

    DELETE FROM abac_tutorial.mapping_demo.user_accessWHERE user_email = current_user() AND region = 'eu';

### Expire access[​](#expire-access "Direct link to Expire access")

Set your access entry to a past date. The row filter UDF checks `expires_on >= current_date()`, so expired entries are silently ignored and access is automatically revoked. This is useful for contractors, data sharing agreements with a fixed duration, or time-limited projects.

SQL

    UPDATE abac_tutorial.mapping_demo.user_accessSET expires_on = current_date() - INTERVAL 1 DAYWHERE user_email = current_user();

Run the following query to verify that you see no rows.

SQL

    SELECT * FROM abac_tutorial.mapping_demo.orders;

Restore access with a future expiration date:

SQL

    UPDATE abac_tutorial.mapping_demo.user_accessSET expires_on = '2099-12-31'WHERE user_email = current_user();

Run the following query to verify that access is restored.

SQL

    SELECT * FROM abac_tutorial.mapping_demo.orders;

## Summary[​](#summary "Direct link to Summary")

This tutorial demonstrated three patterns:

*   **Mapping table pattern**: a single lookup table controls both row filtering and column masking. Access changes are made by updating rows, with no policy or group changes needed.
*   **Conditional masking**: the mask UDF checks the `order_priority` column on each row to decide how to mask PII. Confidential rows are always fully redacted regardless of the user's clearance level, implemented by tagging `order_priority` and passing it to the UDF via `MATCH COLUMNS`.
*   **Access expiration**: the mapping table includes an `expires_on` date. The row filter UDF checks this date against `current_date()`, so expired entries are silently ignored and access auto-revokes with no manual intervention.

## Clean up[​](#clean-up "Direct link to Clean up")

To remove all objects created in this tutorial, run the following.

SQL

    DROP POLICY user_access_filter ON SCHEMA abac_tutorial.mapping_demo;DROP POLICY pii_mask_name ON SCHEMA abac_tutorial.mapping_demo;DROP POLICY pii_mask_email ON SCHEMA abac_tutorial.mapping_demo;DROP FUNCTION IF EXISTS abac_tutorial.mapping_demo.access_filter;DROP FUNCTION IF EXISTS abac_tutorial.mapping_demo.pii_mask;DROP TABLE IF EXISTS abac_tutorial.mapping_demo.orders;DROP TABLE IF EXISTS abac_tutorial.mapping_demo.user_access;DROP SCHEMA IF EXISTS abac_tutorial.mapping_demo CASCADE;

To remove the `region`, `department`, `pii`, and `priority` governed tags, use the Catalog Explorer UI.

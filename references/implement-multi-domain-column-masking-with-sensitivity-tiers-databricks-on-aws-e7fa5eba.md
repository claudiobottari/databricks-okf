---
title: Implement multi-domain column masking with sensitivity tiers | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/multi-domain
ingestedAt: "2026-06-18T08:03:28.414Z"
---

This tutorial shows how to implement domain-aware column masking with sensitivity tiers, combined with region-based row filtering. You use AND conditions in `MATCH COLUMNS` to target columns by both domain and sensitivity level, and `EXCEPT` clauses to exempt each domain's owning group from the corresponding mask policy.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

*   Databricks Runtime 16.4 or above, or serverless compute.
*   Account admin or workspace admin permissions (to create governed tags).
*   `MANAGE` permission on the target catalog or schema.
*   `EXECUTE` on the UDFs.
*   Account groups: `hr_team`, `finance_team`, `marketing_team`, `us_team`, `eu_team`.

To create the required groups, go to **Workspace Settings** > **Identity and access** > **Groups**, click **Add group**, and create each one. Add yourself to at least `hr_team` and `us_team` to follow the HR + US perspective in Step 7.

## Scenario[​](#scenario "Direct link to Scenario")

Your organization maintains a central `employee_records` table shared across HR, Finance, and Marketing. Each team owns certain columns and should see their own data unmasked, but should not see other teams' sensitive data.

The tutorial uses a governed tag called `domain` to represent which team owns each column. The name is arbitrary. You can also use `team`, `department`, or `business_unit`. The key idea is that each column is assigned to exactly one owning group, and a second `sensitivity` tag controls how aggressively the data is masked for users outside that group.

The masking behavior depends on the sensitivity level:

*   **Internal**: users outside the owning group see a partial mask (first character + `***`).
*   **Confidential**: users outside the owning group see `***REDACTED***`.

Users in multiple domain groups see all of their domains' columns unmasked.

Create the following governed tags in the Catalog Explorer UI (**Catalog** > **Govern** > **Governed Tags** > **Create governed tag**):

warning

Tag data is stored as plain text and may be replicated globally. Do not use tag names, values, or descriptors that could compromise the security of your resources. For example, do not use tag names, values or descriptors that contain personal or sensitive information.

## Step 2: Build sample data[​](#step-2-build-sample-data "Direct link to Step 2: Build sample data")

Create a single `employee_records` table shared across HR, Finance, and Marketing. Each sensitive column will be tagged with both a `domain` and a `sensitivity` level in the next step.

SQL

    CREATE CATALOG IF NOT EXISTS abac_tutorial;USE CATALOG abac_tutorial;CREATE SCHEMA IF NOT EXISTS domain_demo;USE SCHEMA domain_demo;

SQL

    CREATE OR REPLACE TABLE employee_records (  id INT,  employee_name STRING,  ssn STRING,  email STRING,  customer_list STRING,  cost_center STRING,  salary_band STRING,  emp_region STRING,  department STRING);INSERT INTO employee_records VALUES  (1, 'Alice Johnson',  '123-45-6789', 'alice@acme.com',  'Tier-1 Enterprise', 'CC-4010', 'Band 7', 'us', 'Engineering'),  (2, 'Bob Smith',      '234-56-7890', 'bob@acme.com',    'SMB Accounts',      'CC-3020', 'Band 5', 'us', 'Sales'),  (3, 'Carol White',    '345-67-8901', 'carol@acme.com',  'Tier-1 Enterprise', 'CC-5010', 'Band 8', 'eu', 'Engineering'),  (4, 'David Lee',      '456-78-9012', 'david@acme.com',  'Growth Segment',    'CC-2010', 'Band 4', 'eu', 'Marketing'),  (5, 'Eva Martinez',   '567-89-0123', 'eva@acme.com',    'Mid-Market',        'CC-4020', 'Band 6', 'us', 'HR');

Tag each sensitive column with both its `domain` and `sensitivity` values. These two tags together allow each policy to target a specific domain and sensitivity combination using AND conditions in `MATCH COLUMNS`. The `emp_region` column gets a key-only `region` tag because the policy only needs to identify the column rather than check a specific value.

SQL

    -- HR domainALTER TABLE employee_records  ALTER COLUMN employee_name SET TAGS ('domain' = 'hr', 'sensitivity' = 'internal');ALTER TABLE employee_records  ALTER COLUMN ssn SET TAGS ('domain' = 'hr', 'sensitivity' = 'confidential');-- Marketing domainALTER TABLE employee_records  ALTER COLUMN email SET TAGS ('domain' = 'marketing', 'sensitivity' = 'internal');ALTER TABLE employee_records  ALTER COLUMN customer_list SET TAGS ('domain' = 'marketing', 'sensitivity' = 'confidential');-- Finance domainALTER TABLE employee_records  ALTER COLUMN cost_center SET TAGS ('domain' = 'finance', 'sensitivity' = 'internal');ALTER TABLE employee_records  ALTER COLUMN salary_band SET TAGS ('domain' = 'finance', 'sensitivity' = 'confidential');-- Region tag for row filteringALTER TABLE employee_records  ALTER COLUMN emp_region SET TAGS ('region' = '');

## Step 4: Create the UDFs[​](#step-4-create-the-udfs "Direct link to Step 4: Create the UDFs")

The row filter UDF accepts the row's region value and an allowed region as a static argument, and returns `TRUE` when they match. Passing the allowed region as a constant keeps the UDF simple and reusable. Each row filter policy targets one group and passes the region that group is authorized to see.

SQL

    CREATE OR REPLACE FUNCTION abac_tutorial.domain_demo.region_filter(region_val STRING, allowed_region STRING)RETURNS BOOLEANRETURN region_val = allowed_region;

Create a partial mask UDF for internal columns and a full redact UDF for confidential columns.

SQL

    CREATE OR REPLACE FUNCTION abac_tutorial.domain_demo.partial_mask(val STRING)RETURNS STRINGRETURN CONCAT(LEFT(val, 1), '***');CREATE OR REPLACE FUNCTION abac_tutorial.domain_demo.redact(val STRING)RETURNS STRINGRETURN '***REDACTED***';

## Step 5: Create the row filter policies[​](#step-5-create-the-row-filter-policies "Direct link to Step 5: Create the row filter policies")

Create one row filter policy per region. Each policy targets a specific group and passes the allowed region as a constant via `USING COLUMNS`.

SQL

    CREATE POLICY region_filter_usON SCHEMA abac_tutorial.domain_demoROW FILTER abac_tutorial.domain_demo.region_filterTO `us_team`FOR TABLESMATCH COLUMNS has_tag('region') AS region_colUSING COLUMNS (region_col, 'us');CREATE POLICY region_filter_euON SCHEMA abac_tutorial.domain_demoROW FILTER abac_tutorial.domain_demo.region_filterTO `eu_team`FOR TABLESMATCH COLUMNS has_tag('region') AS region_colUSING COLUMNS (region_col, 'eu');

note

An alternative is to embed the group logic inside the UDF using identity functions such as `is_account_group_member()`. That approach uses a single policy with no static values, but moves the group-to-region mapping into the UDF. Use whichever fits your organization.

## Step 6: Create the domain column mask policies[​](#step-6-create-the-domain-column-mask-policies "Direct link to Step 6: Create the domain column mask policies")

Create one policy per domain and sensitivity combination. Each policy uses AND to match columns with a specific `domain` AND `sensitivity` level, and `EXCEPT` to exempt the owning domain group.

Because each column has exactly one `domain` value and one `sensitivity` value, each column is matched by exactly one policy per user. There are no conflicts.

### Internal columns (partial mask)[​](#internal-columns-partial-mask "Direct link to Internal columns (partial mask)")

Apply a partial mask to internal-level columns for users outside the owning domain.

SQL

    CREATE POLICY mask_internal_hrON SCHEMA abac_tutorial.domain_demoCOLUMN MASK abac_tutorial.domain_demo.partial_maskTO `account users` EXCEPT `hr_team`FOR TABLESMATCH COLUMNS (  has_tag_value('domain', 'hr')  AND has_tag_value('sensitivity', 'internal')) AS mON COLUMN m;CREATE POLICY mask_internal_financeON SCHEMA abac_tutorial.domain_demoCOLUMN MASK abac_tutorial.domain_demo.partial_maskTO `account users` EXCEPT `finance_team`FOR TABLESMATCH COLUMNS (  has_tag_value('domain', 'finance')  AND has_tag_value('sensitivity', 'internal')) AS mON COLUMN m;CREATE POLICY mask_internal_marketingON SCHEMA abac_tutorial.domain_demoCOLUMN MASK abac_tutorial.domain_demo.partial_maskTO `account users` EXCEPT `marketing_team`FOR TABLESMATCH COLUMNS (  has_tag_value('domain', 'marketing')  AND has_tag_value('sensitivity', 'internal')) AS mON COLUMN m;

### Confidential columns (full redaction)[​](#confidential-columns-full-redaction "Direct link to Confidential columns (full redaction)")

Fully redact confidential-level columns for users outside the owning domain.

SQL

    CREATE POLICY mask_confidential_hrON SCHEMA abac_tutorial.domain_demoCOLUMN MASK abac_tutorial.domain_demo.redactTO `account users` EXCEPT `hr_team`FOR TABLESMATCH COLUMNS (  has_tag_value('domain', 'hr')  AND has_tag_value('sensitivity', 'confidential')) AS mON COLUMN m;CREATE POLICY mask_confidential_financeON SCHEMA abac_tutorial.domain_demoCOLUMN MASK abac_tutorial.domain_demo.redactTO `account users` EXCEPT `finance_team`FOR TABLESMATCH COLUMNS (  has_tag_value('domain', 'finance')  AND has_tag_value('sensitivity', 'confidential')) AS mON COLUMN m;CREATE POLICY mask_confidential_marketingON SCHEMA abac_tutorial.domain_demoCOLUMN MASK abac_tutorial.domain_demo.redactTO `account users` EXCEPT `marketing_team`FOR TABLESMATCH COLUMNS (  has_tag_value('domain', 'marketing')  AND has_tag_value('sensitivity', 'confidential')) AS mON COLUMN m;

## Step 7: Verify the results[​](#step-7-verify-the-results "Direct link to Step 7: Verify the results")

All seven policies (two row filters and six column masks) are now active. Run the following query and verify that the results match what your group membership permits.

SQL

    SELECT * FROM abac_tutorial.domain_demo.employee_records;

**HR team member in US region** (`hr_team` + `us_team`):

HR columns (`employee_name`, `ssn`) are unmasked. Marketing internal (`email`) is partially masked and confidential (`customer_list`) is redacted. Finance internal (`cost_center`) is partially masked and confidential (`salary_band`) is redacted.

**Finance team member in EU region** (`finance_team` + `eu_team`):

Finance columns (`cost_center`, `salary_band`) are unmasked. All other domain columns are masked or redacted.

**User in `hr_team` + `marketing_team` + `us_team`:**

Both HR and Marketing columns are unmasked because the user belongs to both groups. Finance columns remain masked.

## Why this pattern works[​](#why-this-pattern-works "Direct link to Why this pattern works")

Each column has exactly one `domain` value and one `sensitivity` value, so each column is matched by exactly one policy per user. There are no policy conflicts.

The `EXCEPT` clause is the key. Each policy applies to `account users` except the domain group that owns those columns. If you're in the owning group, the policy doesn't apply and you see the raw data. If you aren't, the policy applies and the data is masked. Multi-group users benefit naturally: a user in both `hr_team` and `marketing_team` is excluded from both sets of HR and Marketing policies.

Adding a new domain (for example, Legal) requires:

1.  A new group (`legal_team`).
2.  A new allowed value `legal` for the `domain` tag.
3.  Two new policies (`mask_internal_legal`, `mask_confidential_legal`).
4.  Tags on the new columns.

No existing policies need to change.

## Clean up[​](#clean-up "Direct link to Clean up")

To remove all objects created in this tutorial, run the following.

SQL

    DROP POLICY region_filter_us ON SCHEMA abac_tutorial.domain_demo;DROP POLICY region_filter_eu ON SCHEMA abac_tutorial.domain_demo;DROP POLICY mask_internal_hr ON SCHEMA abac_tutorial.domain_demo;DROP POLICY mask_internal_finance ON SCHEMA abac_tutorial.domain_demo;DROP POLICY mask_internal_marketing ON SCHEMA abac_tutorial.domain_demo;DROP POLICY mask_confidential_hr ON SCHEMA abac_tutorial.domain_demo;DROP POLICY mask_confidential_finance ON SCHEMA abac_tutorial.domain_demo;DROP POLICY mask_confidential_marketing ON SCHEMA abac_tutorial.domain_demo;DROP FUNCTION IF EXISTS abac_tutorial.domain_demo.region_filter;DROP FUNCTION IF EXISTS abac_tutorial.domain_demo.partial_mask;DROP FUNCTION IF EXISTS abac_tutorial.domain_demo.redact;DROP TABLE IF EXISTS abac_tutorial.domain_demo.employee_records;DROP SCHEMA IF EXISTS abac_tutorial.domain_demo CASCADE;

To remove the `region`, `domain`, and `sensitivity` governed tags, and the account groups (`hr_team`, `finance_team`, `marketing_team`, `us_team`, `eu_team`), use the Catalog Explorer UI and workspace settings respectively.

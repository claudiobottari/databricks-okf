---
title: Secure new tables by default with control tags | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/secure-by-default
ingestedAt: "2026-06-18T08:03:36.446Z"
---

This tutorial shows how to lock down new tables automatically and release them only after a data steward has reviewed and classified their contents. It uses:

*   A schema-level `review_status` control tag so every new table in the schema is masked by default
*   [Data Classification](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification) to automatically detect and tag sensitive columns with `class.*` system tags
*   The built-in `system.data_classification.mask_value` function for type-aware masking
*   Two policies: one that masks all columns while a table is pending review, and one that masks only classified columns after review

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

*   Databricks Runtime 16.4 or above, or serverless compute.
*   Account admin or workspace admin permissions (to create governed tags and enable Data Classification).
*   `MANAGE` permission on the target catalog or schema.
*   `EXECUTE` on the UDFs.
*   A SQL notebook or query editor.

## Scenario[​](#scenario "Direct link to Scenario")

Your organization regularly adds new tables to a Unity Catalog schema from acquisitions, partner integrations, or new product features. By default, any user with `SELECT` on the schema can immediately query new tables, including columns that might contain unclassified PII.

The control tag pattern addresses this: a schema-level `review_status = pending` tag causes every new table in the schema to be fully masked by default. Data Classification scans the table in the background and applies `class.*` tags to detected sensitive columns. After a data steward reviews the classifications and corrects any false positives, they flip `review_status` to `reviewed` at the table level. This overrides the inherited schema tag, and a second policy takes over: masking only the `class.*`\-tagged columns while leaving non-sensitive columns accessible.

## Step 1: Enable Data Classification on the catalog[​](#step-1-enable-data-classification-on-the-catalog "Direct link to Step 1: Enable Data Classification on the catalog")

Data Classification scans tables in the background and applies `class.*` system governed tags such as `class.name`, `class.email_address`, and `class.us_ssn`. No custom tags are required for column-level detection.

1.  In Catalog Explorer, select your catalog and go to the **Details** tab.
2.  Next to **Data Classification**, click **Enable**.
3.  Optionally choose which schemas to include.

Automatic tagging is enabled later, from the Data Classification results page after reviewing initial detections (Step 6).

For full details, see [Data Classification](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification).

## Step 2: Create the `review_status` governed tag[​](#step-2-create-the-review_status-governed-tag "Direct link to step-2-create-the-review_status-governed-tag")

Create the following governed tag in the Catalog Explorer UI (**Catalog** > **Govern** > **Governed Tags** > **Create governed tag**):

warning

Tag data is stored as plain text and may be replicated globally. Do not use tag names, values, or descriptors that could compromise the security of your resources. For example, do not use tag names, values or descriptors that contain personal or sensitive information.

## Step 3: Build the schema and apply the control tag[​](#step-3-build-the-schema-and-apply-the-control-tag "Direct link to Step 3: Build the schema and apply the control tag")

Create a schema and set the control tag to `pending`. Every table created in this schema inherits this tag automatically.

SQL

    CREATE CATALOG IF NOT EXISTS abac_tutorial;USE CATALOG abac_tutorial;CREATE SCHEMA IF NOT EXISTS secure_default;ALTER SCHEMA abac_tutorial.secure_default  SET TAGS ('review_status' = 'pending');

## Step 4: Create the pending review policy[​](#step-4-create-the-pending-review-policy "Direct link to Step 4: Create the pending review policy")

When a table has `review_status = pending`, all columns are masked. `MATCH COLUMNS TRUE` matches every column regardless of tags.

`system.data_classification.mask_value` is a type-aware masking function provided by Databricks. It returns a safe placeholder based on the runtime data type. For example, it returns `0` for integers, `DATE '1970-01-01'` for dates, and a SHA-256 hash for strings. No custom UDF is needed.

SQL

    CREATE POLICY review_pending_policyON SCHEMA abac_tutorial.secure_defaultCOLUMN MASK system.data_classification.mask_valueTO `account users`FOR TABLESWHEN has_tag_value('review_status', 'pending')MATCH COLUMNS TRUE AS m ON COLUMN m;

note

To exempt specific groups from the policy, add an `EXCEPT` clause. For example, `TO \`account users\` EXCEPT \`data\_admins\``lets members of the`data\_admins\` group bypass the mask and see unmasked data.

## Step 5: Create a table and verify lockdown[​](#step-5-create-a-table-and-verify-lockdown "Direct link to Step 5: Create a table and verify lockdown")

Create a table in the schema. It inherits `review_status = pending` from the schema, so all columns are masked immediately.

SQL

    CREATE OR REPLACE TABLE abac_tutorial.secure_default.employee_directory (  id INT,  full_name STRING,  personal_email STRING,  ssn_number STRING,  phone STRING,  office_location STRING,  title STRING,  team STRING);INSERT INTO abac_tutorial.secure_default.employee_directory VALUES  (1, 'Alice Johnson',  'alice.j@gmail.com',    '123-45-6789', '555-0101', 'NYC HQ Floor 12',    'Staff Engineer',      'Platform'),  (2, 'Bob Smith',      'bob.smith@yahoo.com',  '234-56-7890', '555-0202', 'LA Office Suite 4',  'Sales Director',      'Enterprise'),  (3, 'Carol White',    'carol.w@outlook.com',  '345-67-8901', '555-0303', 'Chicago Rm 301',     'Senior Engineer',     'Platform'),  (4, 'David Lee',      'david.lee@gmail.com',  '456-78-9012', '555-0404', 'Houston Floor 2',    'Marketing Lead',      'Growth'),  (5, 'Eva Martinez',   'eva.m@hotmail.com',    '567-89-0123', '555-0505', 'Phoenix Building B', 'HR Business Partner', 'People');

Run the following query to confirm that all columns are masked.

SQL

    SELECT * FROM abac_tutorial.secure_default.employee_directory;

## Step 6: Review classifications and enable auto tagging[​](#step-6-review-classifications-and-enable-auto-tagging "Direct link to Step 6: Review classifications and enable auto tagging")

Once Data Classification scans the table (within 24 hours of enabling it), review the detections and enable auto tagging so that `class.*` tags are applied to both existing and future detections.

1.  In Catalog Explorer, select your catalog and go to the **Details** tab.
2.  Next to **Data Classification**, click **View results**.
3.  Review the detections and provide feedback on any mistakes by clicking the **Exclude** icon next to incorrect detections.
4.  Enable automatic tagging for the classification tags you want applied. Tags populate in the next scan (within 24 hours).

For details on the Data Classification UI and automatic tagging, see [View classification results](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification#view-classification-results) and [Enable automatic tagging](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification#enable-automatic-tagging).

For this tutorial, run the following to simulate the `class.*` tags that auto tagging would apply, so you can see the end-to-end flow without waiting for a background scan.

SQL

    -- Simulate Data Classification tags (in production, these are applied automatically)ALTER TABLE abac_tutorial.secure_default.employee_directory  ALTER COLUMN full_name SET TAGS ('class.name' = '');ALTER TABLE abac_tutorial.secure_default.employee_directory  ALTER COLUMN personal_email SET TAGS ('class.email_address' = '');ALTER TABLE abac_tutorial.secure_default.employee_directory  ALTER COLUMN ssn_number SET TAGS ('class.us_ssn' = '');ALTER TABLE abac_tutorial.secure_default.employee_directory  ALTER COLUMN phone SET TAGS ('class.phone_number' = '');

## Step 7: Create the reviewed policy[​](#step-7-create-the-reviewed-policy "Direct link to Step 7: Create the reviewed policy")

When a table is marked as `reviewed`, only columns tagged with `class.*` tags are masked. Non-classified columns become visible.

SQL

    CREATE POLICY review_complete_policyON SCHEMA abac_tutorial.secure_defaultCOLUMN MASK system.data_classification.mask_valueTO `account users`FOR TABLESWHEN has_tag_value('review_status', 'reviewed')MATCH COLUMNS (  has_tag('class.name')  OR has_tag('class.email_address')  OR has_tag('class.us_ssn')  OR has_tag('class.phone_number')  OR has_tag('class.credit_card')  OR has_tag('class.date_of_birth')) AS mON COLUMN m;

## Step 8: Flip the control tag and verify[​](#step-8-flip-the-control-tag-and-verify "Direct link to Step 8: Flip the control tag and verify")

Mark the table as reviewed. The table-level `reviewed` tag overrides the inherited schema-level `pending` tag, so the pending policy no longer applies and the reviewed policy takes over.

SQL

    ALTER TABLE abac_tutorial.secure_default.employee_directory  SET TAGS ('review_status' = 'reviewed');

Run the following query to confirm the change. Columns with `class.*` tags (`full_name`, `personal_email`, `ssn_number`, `phone`) remain masked. Non-classified columns (`id`, `office_location`, `title`, `team`) are now visible.

SQL

    SELECT * FROM abac_tutorial.secure_default.employee_directory;

## Step 9: Verify automatic inheritance for new tables[​](#step-9-verify-automatic-inheritance-for-new-tables "Direct link to Step 9: Verify automatic inheritance for new tables")

Create another table in the same schema. It inherits `review_status = pending` and is fully locked down automatically. No additional configuration is needed.

SQL

    CREATE OR REPLACE TABLE abac_tutorial.secure_default.transaction_log (  txn_id INT, account_holder STRING, amount DOUBLE, txn_date DATE, description STRING);INSERT INTO abac_tutorial.secure_default.transaction_log VALUES  (1001, 'Alice Johnson', 2500.00, '2026-01-15', 'Wire transfer'),  (1002, 'Bob Smith',     1800.00, '2026-01-16', 'Direct deposit'),  (1003, 'Carol White',   4200.00, '2026-01-17', 'Invoice payment');

Run the following query to confirm that the new table is fully masked. After Data Classification scans it, only the `class.*`\-tagged columns remain masked after you flip to `reviewed`.

SQL

    SELECT * FROM abac_tutorial.secure_default.transaction_log;

## Clean up[​](#clean-up "Direct link to Clean up")

To remove all objects created in this tutorial, run the following.

SQL

    DROP POLICY review_pending_policy ON SCHEMA abac_tutorial.secure_default;DROP POLICY review_complete_policy ON SCHEMA abac_tutorial.secure_default;DROP TABLE IF EXISTS abac_tutorial.secure_default.employee_directory;DROP TABLE IF EXISTS abac_tutorial.secure_default.transaction_log;DROP SCHEMA IF EXISTS abac_tutorial.secure_default CASCADE;DROP CATALOG IF EXISTS abac_tutorial;

To remove the `review_status` governed tag, use the Catalog Explorer UI.

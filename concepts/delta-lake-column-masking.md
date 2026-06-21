---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0dd2a98432f5404a33bc21a2c1693ed92b4302361e5c0a9d57e770be1bd080d3
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-column-masking
    - DLCM
    - Delta Lake Column Mapping
    - Delta Lake column mapping
    - Column masking
    - column masking
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
    - file: data-classification-databricks-on-aws.md
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: Delta Lake Column Masking
description: A Delta table security feature that masks column values; incompatible with external metadata sources in Databricks.
tags:
  - delta-lake
  - security
  - data-governance
timestamp: "2026-06-18T11:53:19.228Z"
---

# Delta Lake Column Masking

**Delta Lake Column Masking** is a data governance feature that allows you to obfuscate sensitive data in specific columns of a Delta table at query time. When a column mask is applied, users see a masked version of the data (such as `***` instead of actual values) unless they have explicit permissions to view the unmasked data.^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Overview

Column masking in Delta Lake is part of the broader [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) framework in [Unity Catalog](/concepts/unity-catalog.md). A column mask policy defines a user-defined function (UDF) that transforms the column's values for certain users based on their identity or attributes. The mask is applied transparently when queries are executed, so users never see the underlying sensitive data unless the policy grants them access.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## How Column Masking Works

A column mask is a special type of ABAC policy attached to a catalog or schema in Unity Catalog. The policy specifies:

- A condition that determines when the mask applies (based on the column's governed tags or a custom expression).
- A masking function (a user-defined function registered in Unity Catalog) that transforms the column's output for non-privileged users.

When a user queries a table with masked columns, Unity Catalog evaluates the policy at query time. If the user does not meet the policy's conditions, the masking function is applied transparently to the query results. If the user does meet the conditions (for example, they are in a group with access), the original data is returned.^[data-classification-databricks-on-aws.md, create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Creating a Column Mask Policy

### Prerequisites

- You must have `MANAGE` permission on the catalog or schema where the policy will be attached, or own that securable object.
- A masking function must be registered as a user-defined function in Unity Catalog.
- The function must be accessible via `EXECUTE` permission.^[abac-grant-policies-for-models-beta-databricks-on-aws.md, data-classification-databricks-on-aws.md]

### Using SQL

```sql
CREATE MASK POLICY policy_name
ON { CATALOG | SCHEMA } securable_name
COMMENT 'description'
MASK COLUMN
WHEN condition_expression
FUNCTION masking_function_name();
```

The condition expression typically references [Governed Tags](/concepts/governed-tags.md) applied to columns, such as `has_tag('class.email_address')`. The masking function receives the original column value as input and returns the masked output.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Using Catalog Explorer

1. In your Databricks workspace, click **Catalog**.
2. Select the catalog or schema where you want to attach the policy.
3. Click the **Policies** tab.
4. Click **New policy**.
5. Under **Policy type**, select **Mask column**.
6. Under **Condition**, specify which columns to mask (based on tags or a custom expression).
7. Under **Masking function**, select the UDF to apply.
8. Click **Create policy**.^[data-classification-databricks-on-aws.md]

## Creating Column Masks from Data Classification

The [Data Classification](/concepts/data-classification.md) feature in Unity Catalog automatically detects sensitive columns (such as those containing email addresses, phone numbers, or names) and tags them with classification tags like `class.email_address`. You can then create a column mask policy directly from the classification results:^[data-classification-databricks-on-aws.md]

1. On the **Data Classification** results page, click **Review** next to the classification type you want to protect.
2. Open the **User Access** tab.
3. Click **New policy**.
4. The policy form opens pre-filled with a condition matching the classification tag.
5. Specify a masking function and click **Save**.

To create a single policy covering multiple classification types, modify the `When column` condition to use compound expressions:
```
has_tag("class.name") OR has_tag("class.email_address") OR has_tag("class.phone_number")
```

This approach allows efficient governance of multiple sensitive column types with one policy.^[data-classification-databricks-on-aws.md]

## Column Masking and External Metadata

Delta Lake Column Masking interacts with the External Metadata feature. If a table has column mask policies applied, the External Metadata source is not supported — queries against such tables through External Metadata will fail with the error `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE: COLUMN_MASK`. This means that only streaming tables and materialized views (which do not support column masking) are compatible with External Metadata when column masks are present.^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Key Characteristics

| Aspect | Detail |
|--------|--------|
| Purpose | Obfuscate sensitive column values at query time |
| Mechanism | User-defined function transforms output for non-privileged users |
| Evaluation | Performed at query time by Unity Catalog |
| Scope | Attached to catalog or schema level |
| Compared to Row Filters | Column masks transform column values; row filters restrict which rows are visible |

## Best Practices

- **Use governed tags to drive masking conditions.** Tag-based conditions make policies reusable across many columns without modifying the policy definition.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Centralize masking functions.** Create and maintain masking functions in a shared catalog accessible to all policy definitions.
- **Avoid conflicting policies.** Do not apply multiple column mask policies to the same column, as this can lead to unpredictable behavior.
- **Audit mask changes regularly.** Use [ABAC Policy Audit Logging](/concepts/abac-policy-audit-logging.md) to track when policies are created, modified, or deleted.^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Test masking functions thoroughly.** Ensure masking functions handle edge cases (NULL values, empty strings, special characters) correctly.

## Limitations

- Column masking is not supported on streaming tables or materialized views.
- External Metadata cannot be used with tables that have column mask policies.
- Deleting a column or table is not governed by mask policies.
- `INFORMATION_SCHEMA` does not reflect column mask policies.^[abac-grant-policies-for-models-beta-databricks-on-aws.md, delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Related Concepts

- [Row Filter Policies](/concepts/row-filter-policies.md) — ABAC policies that restrict which rows are visible in a query
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Attribute-based grant policies for model access
- [Data Classification](/concepts/data-classification.md) — Automatic detection and tagging of sensitive data
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that provides ABAC capabilities
- [Governed Tags](/concepts/governed-tags.md) — Tags used to drive policy conditions
- [ABAC Policy Audit Logging](/concepts/abac-policy-audit-logging.md) — Tracking of policy and tag operations

## Sources

- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
- data-classification-databricks-on-aws.md
- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
- abac-grant-policies-for-models-beta-databricks-on-aws.md
- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)
2. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)
3. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
4. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
5. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 42ae316284795ab8d00982302e1e3ae747a863b9ede04ad5b50ed902f58c1e6b
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policies-from-data-classification
    - APFDC
  citations:
    - file: data-classification-databricks-on-aws.md
title: ABAC Policies from Data Classification
description: The practice of creating attribute-based access control policies that mask or restrict sensitive columns based on the classification tags detected by the Data Classification engine.
tags:
  - abac
  - masking
  - access-control
  - governance
timestamp: "2026-06-18T11:27:20.723Z"
---

# ABAC Policies from Data Classification

**ABAC Policies from Data Classification** describes how to use the results of [Data Classification](/concepts/data-classification.md) in Unity Catalog to automatically create [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies that mask sensitive data based on classification tags. Databricks recommends using ABAC policies as the primary method for applying governance controls derived from data classification outputs. ^[data-classification-databricks-on-aws.md]

## Overview

After Data Classification identifies sensitive columns in your catalog (for example, columns tagged with `class.email_address` or `class.phone_number`), you can create an ABAC column mask policy that restricts access to those columns based on user attributes. The policy is built directly from the classification results, ensuring that governance controls align with the automatically detected sensitive data. ^[data-classification-databricks-on-aws.md]

## Creating an ABAC Policy from Classification Results

### For a Single Classification Tag

1. On the **Data Classification** results page, click **Review** next to the classification type you want to protect (for example, "Email Address").
2. Open the **User Access** tab.
3. Click **New policy**.
4. The policy creation form opens pre-filled with a condition that matches the classification tag you selected.
5. Specify a masking function (a user-defined function registered in Unity Catalog) to apply to the matching columns.
6. Click **Save**.

After saving, the policy masks the classified columns for users who do not meet the policy’s conditions. ^[data-classification-databricks-on-aws.md]

### For Multiple Classification Tags

To create a single policy that covers multiple classification types, modify the policy’s `When column` condition from a single tag to a compound expression using the `meets condition` option. Use `has_tag()` with logical operators to include multiple tags:

1. Follow steps 1–3 above for any classification tag.
2. Change **When column** to **meets condition**.
3. In the condition field, enter a Boolean expression combining tags. For example:
   ```
   has_tag("class.name") OR has_tag("class.email_address") OR has_tag("class.phone_number")
   ```
4. Specify a masking function and save.

This approach allows you to create a policy — such as one named "Confidential" — that masks any column tagged with any of the included classifications. ^[data-classification-databricks-on-aws.md]

## Example

The following example creates a policy that masks columns tagged as name, email address, or phone number:

| Setting | Value |
|---------|-------|
| Policy name | Confidential |
| When column | `has_tag("class.name") OR has_tag("class.email_address") OR has_tag("class.phone_number")` |
| Masking function | A function registered in Unity Catalog that returns a redacted value |

All columns in the catalog or schema that carry at least one of the specified governed tags will have the masking function applied when a query is executed by a user who does not have an exception or override. ^[data-classification-databricks-on-aws.md]

## Requirements

- You must have the necessary privileges to create ABAC policies on the target catalog or schema (typically `MANAGE` or ownership).
- The masking function must be a user-defined function registered in Unity Catalog and accessible via `EXECUTE`.
- Governed tags (such as `class.email_address`) must already be applied by Data Classification or manually.
- See [ABAC Policy Requirements and Prerequisites](/concepts/abac-policy-requirements.md) for full details.

## Related Concepts

- [Data Classification](/concepts/data-classification.md) — The feature that automatically identifies and tags sensitive columns
- [Column Mask Policies](/concepts/column-mask-policies.md) — ABAC policies that mask sensitive columns based on conditions
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Attribute-based grant policies for models (Beta)
- [Governed Tags](/concepts/governed-tags.md) — Tags that drive ABAC policy evaluation
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer providing ABAC capabilities

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)

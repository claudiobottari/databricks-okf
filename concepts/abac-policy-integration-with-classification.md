---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9268f69a33ed3e3973ac1e8818d4b3735f9bc565be7864b71e8f8334a3b61f3b
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policy-integration-with-classification
    - APIWC
  citations:
    - file: data-classification-databricks-on-aws.md
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
title: ABAC Policy Integration with Classification
description: Integration between Data Classification and Attribute-Based Access Control (ABAC) allowing users to create masking policies directly from classification results, protecting sensitive data by masking columns based on detected classification tags.
tags:
  - data-governance
  - access-control
  - security
timestamp: "2026-06-19T09:41:02.007Z"
---

# ABAC Policy Integration with Classification

**ABAC Policy Integration with Classification** refers to the workflow of using [Data Classification](/concepts/data-classification.md) results to automatically create and apply [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies in Unity Catalog. This integration enables organizations to discover sensitive data through automated classification and then rapidly implement governance controls — such as column masking — based on the detected classification tags.

## Overview

Data Classification uses an AI agent to automatically scan tables in Unity Catalog and apply governed tags to columns that contain sensitive data (e.g., PII, financial information, healthcare data). Once columns are tagged, administrators can create ABAC policies that reference those tags to control access. The integration streamlines the process from data discovery to policy enforcement, reducing manual effort and ensuring consistent protection across the data estate. ^[data-classification-databricks-on-aws.md]

## Creating ABAC Policies from Classification Results

### From the Data Classification UI

The Data Classification results page provides a direct pathway to create ABAC policies:

1. Navigate to the Data Classification results page for a catalog.
2. Click **Review** for a specific classification tag (e.g., `class.email_address`).
3. Open the **User Access** tab.
4. Click **New policy**.

The policy form is pre-filled to mask columns that have the selected classification tag. To complete the policy, specify any masking function registered in Unity Catalog and click **Save**. ^[data-classification-databricks-on-aws.md]

### Creating Policies Covering Multiple Tags

To create a policy that covers multiple classification tags, modify the column condition in the policy form. Change **When column** to **meets condition** and provide a logical expression combining multiple tags.

For example, to create a policy called "Confidential" that masks any name, email, or phone number, set the condition to:

```
has_tag("class.name") OR has_tag("class.email_address") OR has_tag("class.phone_number")
```

^[data-classification-databricks-on-aws.md]

## How the Integration Works

The integration relies on governed tags applied by Data Classification. When automatic tagging is enabled for a classification type, all existing and future detections of that classification are tagged. ABAC policies then use tag-matching functions (such as `has_tag()` and `has_tag_value()`) in their `MATCH COLUMNS` clause to identify which columns to protect. ^[data-classification-databricks-on-aws.md]

Because ABAC policies evaluate at query time against tags on the target column, they automatically cover newly classified columns without requiring policy updates. This creates a dynamic governance layer that adapts as new sensitive data is discovered. ^[data-classification-databricks-on-aws.md]

## Viewing Existing Policies

On the Data Classification results page, the **User Access** tab for each classification tag displays any ABAC policies already assigned to that tag. This allows administrators to see which governance controls are in place for each type of sensitive data. ^[data-classification-databricks-on-aws.md]

## Best Practices

- **Enable automatic tagging** for classification types you intend to govern. This ensures that all detected columns receive the appropriate tags, making them eligible for ABAC policy enforcement. ^[data-classification-databricks-on-aws.md]
- **Review detections before creating policies.** Use the review panel to verify that classifications are accurate. Exclude any incorrect detections to prevent unintended masking. ^[data-classification-databricks-on-aws.md]
- **Use catalog-level ABAC policies** when possible. Attaching a policy at the catalog scope applies it to all tables in that catalog, reducing per-table configuration. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Combine multiple tags in a single policy** to create comprehensive rules (e.g., mask all PII columns regardless of the specific PII subtype). ^[data-classification-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md) — Automated discovery and tagging of sensitive data
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) — Dynamic column masking based on tag conditions
- [Governed Tags](/concepts/governed-tags.md) — The attribute system used by both classification and ABAC
- [ABAC GRANT Policies](/concepts/abac-grant-policies.md) — Dynamic privilege grants (currently for models)
- Supported Classification Tags — The full list of tags Data Classification can apply
- [Data Classification System Table](/concepts/data-classification-system-table.md) — The `system.data_classification.results` table storing classification metadata

## Sources

- data-classification-databricks-on-aws.md
- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
2. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)

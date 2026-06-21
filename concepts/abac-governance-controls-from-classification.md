---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea8d06561226a0b0be41a91e4d79b33e85998a324b66fc7761822a021216c5b8
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-governance-controls-from-classification
    - AGCFC
  citations:
    - file: data-classification-databricks-on-aws.md
title: ABAC Governance Controls from Classification
description: Using Attribute-based Access Control (ABAC) policies in Unity Catalog to mask sensitive columns based on detected classification tags, optionally combining multiple tags in a single policy.
tags:
  - abac
  - access-control
  - masking
  - governance
timestamp: "2026-06-18T14:58:43.892Z"
---

# ABAC Governance Controls from Classification

**ABAC Governance Controls from Classification** describes how the automatic [Data Classification](/concepts/data-classification.md) results in Unity Catalog serve as the foundation for creating [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies. By combining the AI-driven detection of sensitive data with ABAC’s tag-based policy engine, data teams can rapidly discover, tag, and protect columns containing PII, financial data, or other regulated content without manually inspecting every table.

## Overview

Databricks Data Classification uses an agentic AI system to automatically classify and tag tables in Unity Catalog. This creates a rich set of [Governed Tags](/concepts/governed-tags.md) (for example, `class.ssn`, `class.email_address`, `class.phone_number`) that can drive downstream governance. The recommended way to act on those classifications is by creating ABAC policies that reference the same tags — allowing organisations to mask sensitive columns or restrict access based on the classification results. ^[data-classification-databricks-on-aws.md]

## Creating an ABAC Policy from Classification Results

From the Data Classification results page, users can create a new ABAC column mask policy directly in the UI:

1. Review a classification tag by clicking **Review** in the results table.
2. Open the **User Access** tab.
3. Click **New policy**.

The policy form is pre-filled to mask columns that carry the classification tag being reviewed. To apply the mask, specify any masking function that has been registered in Unity Catalog and click **Save**. ^[data-classification-databricks-on-aws.md]

The review panel also displays any existing ABAC policies that are already assigned to that classification tag, providing visibility into current governance coverage. ^[data-classification-databricks-on-aws.md]

### Multi-Tag Policies

A single ABAC policy can cover multiple classification tags by using a compound condition in the `MATCH COLUMNS` clause. For example, to create a policy called “Confidential” that masks any column tagged with `class.name`, `class.email_address`, or `class.phone_number`, specify:

```sql
has_tag("class.name") OR has_tag("class.email_address") OR has_tag("class.phone_number")
```

This is done from the UI by changing the **When column** option to **meets condition** and entering the logical expression. ^[data-classification-databricks-on-aws.md]

## How It Works

ABAC policies created from classification results follow the same mechanics as [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md). The policy evaluates at query time: if a column carries the classification tag, the policy applies the masking UDF to users who are subject to the policy (typically `account users` except exempt groups like compliance teams). Because the policies reference tags rather than hard-coded column names, they automatically cover new columns that receive the same classification tag in future scans. ^[data-classification-databricks-on-aws.md]

## Benefits

- **Automated discovery**: Data Classification finds sensitive columns without manual effort, and ABAC policies can be created in a few clicks from the review panel.
- **Self-service governance**: Non-admin users can create policies from the same interface where they review detection results, reducing the need for central governance teams to handle every request.
- **Dynamic protection**: Policies continue to apply as new data is ingested and classified, ensuring consistent masking without policy maintenance.
- **Auditability**: The **User Access** tab in the classification UI shows which users have masked vs. unmasked access to each classification tag, alongside the associated policies.

## Related Concepts

- [Data Classification](/concepts/data-classification.md) – The AI agent that produces the governed tags used by ABAC policies.
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) – The specific policy type recommended for masking classified columns.
- [ABAC Row Filter Policies](/concepts/abac-row-filter-policies.md) – Alternative policy type that can also reference classification tags.
- [Governed Tags](/concepts/governed-tags.md) – The tagging system that bridges classification and ABAC.
- [Data Classification Results System Table](/concepts/data-classification-results-system-table.md) – The underlying `system.data_classification.results` table that stores detection data.
- GDPR Discovery and Deletion – A use case supported by combining classification with ABAC.

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)

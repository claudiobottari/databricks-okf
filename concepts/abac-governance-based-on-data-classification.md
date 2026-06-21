---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 858e6c19736a71576fcb34ab79f139bab956c9c9e4d971e5f05977c552063ea1
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-governance-based-on-data-classification
    - AGBODC
  citations:
    - file: data-classification-databricks-on-aws.md
title: ABAC Governance based on Data Classification
description: Using attribute-based access control (ABAC) policies in Unity Catalog to mask sensitive data based on classification tags, with the ability to create policies directly from the Data Classification UI.
tags:
  - data-governance
  - abac
  - access-control
  - security
timestamp: "2026-06-19T14:40:35.977Z"
---

# ABAC Governance based on Data Classification

**ABAC Governance based on Data Classification** refers to the practice of using [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) in Unity Catalog to enforce data access policies that are automatically derived from [Data Classification](/concepts/data-classification.md) results. When sensitive data is detected and tagged by the classification engine, administrators can create ABAC policies that mask or restrict access to those columns based on user attributes, without manually identifying which columns to protect. ^[data-classification-databricks-on-aws.md]

## Overview

Databricks Data Classification uses an AI agent to automatically classify and tag tables in Unity Catalog, identifying sensitive data categories such as personal identifiers, financial information, and health records. After classification, the recommended next step is to apply governance controls using ABAC, which evaluates user attributes and data tags at query time to decide whether to mask or allow access. ^[data-classification-databricks-on-aws.md]

ABAC policies can be created directly from the Data Classification results page. The policy form is pre-filled with the classification tag being reviewed, so administrators can quickly create a masking policy for a specific sensitive data type without needing to construct tag predicates manually. ^[data-classification-databricks-on-aws.md]

## Creating an ABAC Policy from Classification Results

To create an ABAC policy based on a classification tag:

1. On the Data Classification results page, click **Review** for the classification tag of interest.
2. Open the **User Access** tab.
3. Click **New policy**.
4. The policy form is pre-filled to mask columns that have the selected classification tag. Admins must specify a masking function registered in Unity Catalog (e.g., `mask_string`, `hash`, or a custom function) and then click **Save**. ^[data-classification-databricks-on-aws.md]

### Multi-Tag Policies

A single ABAC policy can cover multiple classification tags by changing the condition from a single tag check to a logical expression. In the policy form, set **When column** to **meets condition** and provide a condition that references multiple tags. ^[data-classification-databricks-on-aws.md]

**Example:** To create a policy called "Confidential" that masks any column tagged with name, email, or phone number, use the following condition:

```text
has_tag("class.name") OR has_tag("class.email_address") OR has_tag("class.phone_number")
```

## ABAC Policy Evaluation

ABAC policies are evaluated at query time based on the tags present on the column and the attributes of the user executing the query. When a user runs a query against a table, Unity Catalog checks whether the user’s attributes satisfy the policy conditions. If the user is not authorized for unmasked access, the masking function defined in the policy is applied to the returned data. ^[data-classification-databricks-on-aws.md]

Administrators can monitor "masked vs. unmasked" access for each classification tag from the **User Access** tab, which shows the number of distinct users who accessed data in each mode over the last 7 days. This helps assess how effectively the ABAC policy is protecting sensitive data. ^[data-classification-databricks-on-aws.md]

## Prerequisites

To create ABAC policies using classification results, the following permissions are required:

- `USE CATALOG` on the catalog containing the sensitive data.
- `MANAGE` or (`SELECT` + `USE SCHEMA`) to view classification results.
- `SELECT` on the `system.data_classification.results` system table to see sample values in the UI.
- `ASSIGN` on any governed tags referenced in the policy (typically only account admins have this by default; they can grant it to others). ^[data-classification-databricks-on-aws.md]

## Best Practices

- **Verify classification accuracy** before creating ABAC policies. Use the review panel to exclude any incorrect detections. Excluding a detection removes its tag and prevents future re‑application, which keeps policies from masking non‑sensitive columns. ^[data-classification-databricks-on-aws.md]
- **Combine related tags into a single policy** to simplify governance. For example, all personal identification tags (name, email, phone) can be covered by one "Confidential" policy. ^[data-classification-databricks-on-aws.md]
- **Monitor user access** after deploying a policy. The **User Access** tab provides visibility into who is hitting masked vs. unmasked data, allowing fine‑tuning of policy conditions. ^[data-classification-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC) in Unity Catalog](/concepts/attribute-based-access-control-abac-in-unity-catalog.md)
- [Data Classification](/concepts/data-classification.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Masking policies](/concepts/column-mask-policies.md)
- [System tables for data classification](/concepts/unity-catalog-data-classification.md)
- [Governed Tags](/concepts/governed-tags.md)

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)

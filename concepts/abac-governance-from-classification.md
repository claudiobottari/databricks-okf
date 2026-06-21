---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fd8bafd01deab4a58d5a5b0d6d099b596e68aee03d3af7fb942542cd5bae40ad
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-governance-from-classification
    - AGFC
  citations:
    - file: data-classification-databricks-on-aws.md
title: ABAC Governance from Classification
description: Using attribute-based access control policies in Unity Catalog to mask or restrict sensitive columns based on data classification tags detected by the classification engine.
tags:
  - access-control
  - governance
  - security
  - unity-catalog
timestamp: "2026-06-19T18:04:07.398Z"
---

# ABAC Governance from Classification

**ABAC Governance from Classification** refers to the practice of using [Databricks Data Classification](/concepts/databricks-data-classification.md) results to automatically create [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac-in-unity-catalog.md) policies that govern access to sensitive data. By combining the automated discovery of sensitive columns with ABAC’s fine-grained access rules, organizations can enforce masking, filtering, or permission restrictions based on the classification tags assigned to each column.

## Overview

Databricks Data Classification uses an AI agent to scan tables in Unity Catalog and assign classification tags (such as `class.name`, `class.email_address`, `class.phone_number`) to columns that contain sensitive data. Once columns are tagged, you can use ABAC to create policies that mask or restrict access to those columns, based on user attributes or other conditions. This workflow enables a governance model where sensitive data is first discovered and then automatically protected. ^[data-classification-databricks-on-aws.md]

## How to create an ABAC policy from classification results

1. On the **Data Classification** results page, locate the classification type (for example, **Name** or **Email**) you want to protect.
2. Click **Review** in the rightmost column to open the review panel.
3. Select the **User Access** tab.
4. Click **New policy**. The policy form is pre‑filled to mask all columns that have the selected classification tag. ^[data-classification-databricks-on-aws.md]
5. Specify a masking function that is already registered in Unity Catalog—this determines how the data is transformed for users who do not meet the policy conditions.
6. Click **Save** to create the ABAC policy. ^[data-classification-databricks-on-aws.md]

The new policy is immediately active, and any column tagged with that classification will be masked according to the specified masking function.

## Multi‑tag policies

You can create a single ABAC policy that covers multiple classification tags. In the policy editor, change the condition from **When column** to **meets condition** and provide a logical expression combining several tags. For example:

- `has_tag("class.name") OR has_tag("class.email_address") OR has_tag("class.phone_number")`

This allows you to define a single policy—such as “Confidential”—that masks any column containing name, email, or phone number data. ^[data-classification-databricks-on-aws.md]

## Requirements

- The user creating the ABAC policy must have appropriate permissions on the classification tag and the catalog. The source material does not specify the exact permissions for ABAC policy creation, but for viewing classification results and enabling automatic tagging, users need `USE CATALOG`, `APPLY TAG`, and `ASSIGN` on the tag. The same privileges likely apply when creating policies from the Data Classification UI. ^[data-classification-databricks-on-aws.md]
- The masking function must be registered in Unity Catalog before it can be selected in the policy form.

## Related concepts

- [Attribute-Based Access Control (ABAC) in Unity Catalog](/concepts/attribute-based-access-control-abac-in-unity-catalog.md) — The underlying mechanism for creating fine‑grained access rules using tags and other attributes.
- [Data Classification](/concepts/data-classification.md) — The automated scanning and tagging of sensitive data in Unity Catalog.
- [Governed Tags](/concepts/governed-tags.md) — System‑defined tags used by Data Classification, which require `ASSIGN` permission to be applied in policies.
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer that supports ABAC and Data Classification.
- ai_mask Function|Masking function — A registered Unity Catalog function that transforms data at query time.

## Benefits

- **Automated discovery**: Sensitive columns are identified without manual inspection.
- **Dynamic enforcement**: ABAC policies automatically apply to both existing and newly classified columns.
- **Reduced overhead**: A single multi‑tag policy can cover many sensitive data types, simplifying governance.

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)

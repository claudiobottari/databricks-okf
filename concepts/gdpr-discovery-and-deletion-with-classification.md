---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 73097ef139d6c1af8f3023f3db4a5120f48c19094e6c905dc242322c439e8950
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gdpr-discovery-and-deletion-with-classification
    - Deletion with Classification and GDPR Discovery
    - GDADWC
  citations:
    - file: data-classification-databricks-on-aws.md
title: GDPR Discovery and Deletion with Classification
description: A use case and example notebook showing how to leverage data classification results to assist with data discovery and deletion for GDPR compliance.
tags:
  - compliance
  - gdpr
  - data-governance
timestamp: "2026-06-19T18:04:35.582Z"
---

# GDPR Discovery and Deletion with Classification

**GDPR Discovery and Deletion with Classification** is a methodology within [Databricks Data Classification](/concepts/databricks-data-classification.md) that enables organizations to identify and manage personal data subject to General Data Protection Regulation (GDPR) compliance requirements. The approach combines automated data classification with governance controls to support both data discovery and deletion workflows.

## Overview

GDPR requires organizations to be able to discover, locate, and delete personal data upon request. Databricks Data Classification provides a practical framework for meeting these obligations by using an AI-powered classification engine that automatically identifies and tags sensitive data across [Unity Catalog](/concepts/unity-catalog.md).^[data-classification-databricks-on-aws.md]

## Key Capabilities

The GDPR discovery and deletion workflow using data classification enables:

- **Data discovery**: Automatically identify columns containing personally identifiable information (PII) and other regulated data types across your catalog.^[data-classification-databricks-on-aws.md]
- **Classification review**: Review detected classifications and verify their accuracy through the Data Classification results interface.^[data-classification-databricks-on-aws.md]
- **Deletion assistance**: Use classification results to guide data deletion processes required for GDPR compliance, such as right-to-erasure requests.^[data-classification-databricks-on-aws.md]

## How It Works

### Enable Classification

1. Ensure your workspace has [serverless compute](/concepts/serverless-gpu-compute.md) available (enabled by default in workspaces with Unity Catalog).^[data-classification-databricks-on-aws.md]
2. Enable Data Classification on your catalogs by navigating to the Data Classification results page and clicking **Configure**, then selecting the catalogs you want to enable.^[data-classification-databricks-on-aws.md]
3. The classification engine will incrementally scan all tables in the selected catalog, with new tables and columns typically classified within 24 hours.^[data-classification-databricks-on-aws.md]

### Review and Correct Classifications

After classification, review the detected columns for each classification type. If the classification engine has incorrectly identified a column as containing regulated data, you can:

1. Open the review panel for the relevant classification tag.
2. Click the **Exclude** icon next to the incorrect detection.
3. This action removes the tag, prevents reapplication in future scans, and provides feedback to improve classification accuracy.^[data-classification-databricks-on-aws.md]

### Apply Governance Controls

Databricks recommends using [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) in Unity Catalog to create governance policies based on classification results. From the Data Classification results page, you can:

1. Click **Review** for a classification tag.
2. Open the **User Access** tab.
3. Click **New policy** to create an ABAC policy that masks columns matching specific classification tags.

For example, to create a GDPR compliance policy that masks any name, email, or phone number, set the condition to `has_tag("class.name") OR has_tag("class.email_address") OR has_tag("class.phone_number")`.^[data-classification-databricks-on-aws.md]

## Practical Workflow

The following example notebook demonstrates how to use Data Classification for GDPR data discovery and deletion:

- **GDPR discovery and deletion using data classification notebook** — A practical guide for implementing GDPR compliance workflows using classification results.^[data-classification-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md) — The core feature for automated tagging of sensitive data
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform for managing classification results
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Recommended approach for creating governance controls
- Supported Classification Tags — Full list of supported tags including PII, GDPR, and other compliance frameworks
- GDPR Compliance — Broader regulatory requirements for data protection
- Right to Erasure — The GDPR principle requiring data deletion upon request

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)

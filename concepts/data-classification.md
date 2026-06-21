---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60fd42cd949d87f0aad05ca18ac9c4a5cbd1c3dff18f4847ebb98cdb6edb39fc
  pageDirectory: concepts
  sources:
    - get-started-with-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-classification
    - AutoML Classification
    - Classification
    - Data Classification Tags
    - Data Classification Types
    - classification
    - Built-in classification tags
    - Classification Problem Type
    - Data Classification limitations
    - classification tag
  citations:
    - file: get-started-with-unity-catalog-databricks-on-aws.md
title: Data Classification
description: AI-agent-based automatic scanning of catalog data to tag sensitive information such as PII, financial data, and credentials, which can integrate with ABAC policies.
tags:
  - data-governance
  - classification
  - pii
timestamp: "2026-06-19T19:00:54.546Z"
---

# Data Classification

**Data Classification** in [Unity Catalog](/concepts/unity-catalog.md) is an AI-driven feature that automatically scans your catalog and tags sensitive data, such as personally identifiable information (PII), financial information, and credentials. This automated tagging helps organizations identify and govern sensitive assets without manual inspection. ^[get-started-with-unity-catalog-databricks-on-aws.md]

## How It Works

Data Classification uses an AI agent to scan tables and columns across the catalog. It recognizes patterns and metadata that indicate sensitive content and applies tags accordingly. The classification results are displayed in a dedicated page within the Unity Catalog UI. ^[get-started-with-unity-catalog-databricks-on-aws.md]

## Integration with Access Control

After classification, the tags can be used directly with [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies. This enables dynamic, policy-driven governance: instead of managing permissions table by table, you write ABAC rules that reference the classification tags. For example, you can automatically mask columns tagged as `PII` or restrict access to financial data for non‑privileged roles. ^[get-started-with-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that provides the scanning infrastructure.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – A policy engine that uses classification tags for fine-grained access control.
- Personally Identifiable Information (PII) – A common category detected by classification.
- Data Governance – The broader practice of managing data availability, usability, and security.

## Sources

- get-started-with-unity-catalog-databricks-on-aws.md

# Citations

1. [get-started-with-unity-catalog-databricks-on-aws.md](/references/get-started-with-unity-catalog-databricks-on-aws-3c48b4d4.md)

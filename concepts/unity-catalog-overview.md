---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 92b3f40eee0de906ccb5e1ebfc5f39637106194b0a0efcbcd11b8e8d529e017b
  pageDirectory: concepts
  sources:
    - get-started-with-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-overview
    - UCO
    - Unity Catalog Views
    - Unity Catalog view
  citations:
    - file: get-started-with-unity-catalog-databricks-on-aws.md
title: Unity Catalog Overview
description: The unified governance layer for data and AI in Databricks, providing centralized access control, lineage, auditing, and data discovery
tags:
  - data-governance
  - databricks
  - catalog
timestamp: "2026-06-19T10:45:24.560Z"
---

Here is the wiki page for "Unity Catalog Overview", written based solely on the provided source material.

---

## Unity Catalog Overview

**Unity Catalog** is the unified governance layer for data and AI in Databricks. It provides centralized access control, lineage, auditing, and data discovery across your workspaces. ^[get-started-with-unity-catalog-databricks-on-aws.md]

Unity Catalog is automatically enabled for all Databricks workspaces created after November 8, 2023. For workspaces that predate Unity Catalog or were not enabled at creation, an upgrade guide is available to enable Unity Catalog and migrate existing data. ^[get-started-with-unity-catalog-databricks-on-aws.md]

## Core Capabilities

### Attribute-Based Access Control (ABAC)

[Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) allows you to define dynamic, fine-grained access policies based on attributes of the data and the user accessing it. Instead of managing permissions table by table, you write policies that automatically enforce row-level filtering and column-level masking. For example, you can hide sensitive columns from users outside a specific region or mask PII for non-privileged roles. ^[get-started-with-unity-catalog-databricks-on-aws.md]

### Data Classification

[Data Classification](/concepts/data-classification.md) uses an AI agent to automatically scan your catalog and tag sensitive data such as PII, financial information, and credentials. After classification, tags can integrate directly with ABAC policies, allowing you to apply governance controls based on what the data actually contains rather than managing access object by object. ^[get-started-with-unity-catalog-databricks-on-aws.md]

### Data Quality Monitoring

[Data Quality Monitoring](/concepts/data-quality-monitoring.md) provides anomaly detection across all tables in a schema and data profiling at the table level. Anomaly detection automatically monitors freshness and completeness using historical data patterns, surfacing issues without manual configuration. Data profiling captures statistical distributions over time, enabling you to track data integrity and set alerts for unexpected changes. ^[get-started-with-unity-catalog-databricks-on-aws.md]

### Data Lineage

[Data Lineage](/concepts/data-lineage.md) automatically captures how data flows across tables, notebooks, jobs, and pipelines — down to the column level. You can trace the origin of any column, see what downstream assets depend on it, and understand the full impact of a schema change before making it. ^[get-started-with-unity-catalog-databricks-on-aws.md]

### AI Governance with Unity AI Gateway

[Unity AI Gateway](/concepts/unity-ai-gateway.md) extends Unity Catalog governance to AI. It provides enterprise governance for LLM endpoints, agents, and MCP servers, allowing you to implement access control, audit logging, and observability across all AI interactions in a unified UI. ^[get-started-with-unity-catalog-databricks-on-aws.md]

## Getting Started

- **Unity Catalog setup guide**: For workspaces with Unity Catalog already enabled. Configure admin roles, users, compute, permissions, and catalogs. ^[get-started-with-unity-catalog-databricks-on-aws.md]
- **Upgrade to Unity Catalog**: For existing workspaces not yet on Unity Catalog. Enable Unity Catalog and migrate your data. ^[get-started-with-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [What is Unity Catalog?](/concepts/unity-catalog.md)
- Unity Catalog best practices
- [Metastore](/concepts/metastore.md)
- Data Governance

## Sources

- get-started-with-unity-catalog-databricks-on-aws.md

# Citations

1. [get-started-with-unity-catalog-databricks-on-aws.md](/references/get-started-with-unity-catalog-databricks-on-aws-3c48b4d4.md)

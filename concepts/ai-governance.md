---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9b74208e083ec6373247de8dfa3f88b5c0ca9848b348a1a1cdfb7e0b5b82cb59
  pageDirectory: concepts
  sources:
    - ai-governance-databricks-on-aws.md
    - what-is-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - ai-governance
    - Data Governance
    - Data governance
    - Tag Governance
    - data governance
    - governance
    - Model Governance
    - model governance
  citations:
    - file: ai-governance-databricks-on-aws.md
    - file: what-is-unity-catalog-databricks-on-aws.md
title: AI Governance
description: Extending data governance frameworks to AI resources, applying access control, lineage, and audit models to AI assets and AI traffic.
tags:
  - governance
  - AI
  - data-management
timestamp: "2026-06-19T17:28:47.652Z"
---

# AI Governance

**AI Governance** on Databricks extends the data governance capabilities of [Unity Catalog](/concepts/unity-catalog.md) to AI resources, applying the same access control, lineage, and audit model that protects data assets to AI assets and AI traffic. ^[ai-governance-databricks-on-aws.md]

## AI Asset Governance with Unity Catalog

Unity Catalog manages AI assets as [securable objects](/concepts/unity-catalog-securable-objects.md), allowing administrators to grant and revoke access using standard Unity Catalog privileges. The following AI assets are governed: ^[ai-governance-databricks-on-aws.md]

- **Models** – Registered ML models in Unity Catalog. See Model Lifecycle Management.
- **Functions** – Unity Catalog functions used as agent tools or for data transformations. See Create AI Agent Tools.
- **Connections** – Unity Catalog HTTP connections used to access external APIs and MCP servers. See HTTP Connections.
- **Hosted foundation models** – Databricks-hosted foundation models available through Foundation Model APIs. See [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md).

These assets follow the same three-level namespace (`catalog.schema.object`) as other Unity Catalog securable objects, ensuring consistent governance across data and AI resources. ^[what-is-unity-catalog-databricks-on-aws.md]

## AI Traffic Governance with Unity AI Gateway

> **Beta** – This feature is in Beta. Account admins can control access from the account console **Previews** page.

[Unity AI Gateway](/concepts/unity-ai-gateway.md) serves as the enterprise control plane for governing AI traffic across an organization. It allows centralized management and monitoring of LLM endpoints and MCP servers: ^[ai-governance-databricks-on-aws.md]

- **LLMs** – Control access to hosted and external LLM endpoints, enforce rate limits, and track usage and costs across providers.
- **MCPs** – Manage access to managed, external, and custom MCP servers alongside LLM endpoints.

Together with Unity Catalog, Unity AI Gateway provides a unified governance layer for both AI assets and AI traffic. ^[ai-governance-databricks-on-aws.md]

## Relationship to Unity Catalog

AI governance is built on top of Unity Catalog, which is the unified governance layer automatically enabled for Databricks workspaces created after November 8, 2023. Unity Catalog provides built-in capabilities for Access Control, [Data Lineage](/concepts/data-lineage.md), Auditing, [Data Classification](/concepts/data-classification.md), [Data Quality Monitoring](/concepts/data-quality-monitoring.md), and [Data Sharing](/concepts/delta-sharing.md). AI governance adds governance of AI-specific resources to this framework. ^[what-is-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Unity AI Gateway](/concepts/unity-ai-gateway.md)
- Securable Objects
- Access Control
- [Data Lineage](/concepts/data-lineage.md)
- Auditing
- Model Lifecycle Management
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Delta Sharing](/concepts/delta-sharing.md)

## Sources

- ai-governance-databricks-on-aws.md
- what-is-unity-catalog-databricks-on-aws.md

# Citations

1. [ai-governance-databricks-on-aws.md](/references/ai-governance-databricks-on-aws-e6fd4910.md)
2. [what-is-unity-catalog-databricks-on-aws.md](/references/what-is-unity-catalog-databricks-on-aws-ea58b0e9.md)

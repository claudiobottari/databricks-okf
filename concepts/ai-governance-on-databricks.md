---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 57607f894cbc2b3c2725a85e1caa1672a9c0865a92aaa88386d483683ddef9d3
  pageDirectory: concepts
  sources:
    - ai-governance-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-governance-on-databricks
    - AGOD
    - Data Governance in Databricks
    - Data Governance on Databricks
    - Data governance on Databricks
    - Model Governance on Databricks
  citations:
    - file: ai-governance-databricks-on-aws.md
title: AI Governance on Databricks
description: Extends data governance capabilities of Unity Catalog to AI resources, applying access control, lineage, and audit models to AI assets and AI traffic.
tags:
  - ai-governance
  - data-governance
  - databricks
timestamp: "2026-06-19T13:55:30.365Z"
---

# AI Governance on Databricks

**AI Governance on Databricks** refers to the framework for managing, securing, and monitoring AI assets and AI traffic within the Databricks platform. It extends the data governance capabilities of [Unity Catalog](/concepts/unity-catalog.md) to AI resources, applying the same access control, lineage, and audit model that protects data assets to AI assets and AI traffic.^[ai-governance-databricks-on-aws.md]

## AI Asset Governance with Unity Catalog

Unity Catalog manages AI assets as securable objects. You can grant and revoke access to the following AI assets using standard Unity Catalog privileges:^[ai-governance-databricks-on-aws.md]

- **Models**: Registered ML models in Unity Catalog. See Manage model lifecycle.
- **Functions**: Unity Catalog functions used as agent tools or for data transformations. See Create AI agent tools using Unity Catalog functions.
- **Connections**: Unity Catalog HTTP connections used to access external APIs and MCP servers. See HTTP connections.
- **Hosted foundation models**: Databricks-hosted foundation models available through Foundation Model APIs. See [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md).

## AI Traffic Governance with Unity AI Gateway

**Beta** — This feature is in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types). Account admins can control access to this feature from the account console **Previews** page.^[ai-governance-databricks-on-aws.md]

[Unity AI Gateway](/concepts/unity-ai-gateway.md) is the enterprise control plane for governing AI traffic across your organization. Use Unity AI Gateway to manage and monitor LLM endpoints and MCP servers from a central location:^[ai-governance-databricks-on-aws.md]

- **LLMs**: Control access to hosted and external LLM endpoints, enforce rate limits, and track usage and costs across providers.
- **MCPs**: Manage access to managed, external, and custom MCP servers alongside your LLM endpoints.

## Key Capabilities

AI governance on Databricks provides several key capabilities that unify data and AI governance:^[ai-governance-databricks-on-aws.md]

| Capability | Description |
|------------|-------------|
| **Access Control** | Grant and revoke permissions on models, functions, connections, and hosted foundation models using Unity Catalog privileges |
| **Lineage** | Track the lineage of AI assets alongside data assets |
| **Audit** | Maintain audit logs for all AI asset operations |
| **Traffic Management** | Govern LLM endpoint access, enforce rate limits, and monitor usage and costs |

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The underlying governance framework for data and AI assets
- Model Lifecycle Management — Managing registered ML models in Unity Catalog
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Databricks-hosted foundation model endpoints
- Agent Framework — Creating AI agent tools governed by Unity Catalog functions
- HTTP Connections — External API access managed through Unity Catalog

## Sources

- ai-governance-databricks-on-aws.md

# Citations

1. [ai-governance-databricks-on-aws.md](/references/ai-governance-databricks-on-aws-e6fd4910.md)

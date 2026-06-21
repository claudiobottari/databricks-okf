---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 471dd07dfc18a25e655ec15471059e699144bba185d3c8664c179a2266cfbec2
  pageDirectory: concepts
  sources:
    - ai-governance-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-governance-with-unity-catalog
    - AGWUC
    - AI Asset Governance with Unity Catalog
    - Data Governance with Unity Catalog
    - Trace Governance with Unity Catalog
  citations:
    - file: ai-governance-databricks-on-aws.md
title: AI Governance with Unity Catalog
description: Extending Databricks' data governance capabilities (access control, lineage, audit) to AI assets such as models, functions, connections, and hosted foundation models using Unity Catalog.
tags:
  - ai-governance
  - unity-catalog
  - databricks
timestamp: "2026-06-19T08:54:41.459Z"
---

# AI Governance with Unity Catalog

**AI governance** extends the data governance capabilities of [Unity Catalog](/concepts/unity-catalog.md) to AI resources, applying the same access control, lineage, and audit model that protects data assets to AI assets and AI traffic.^[ai-governance-databricks-on-aws.md]

## AI Asset Governance with Unity Catalog

Unity Catalog manages AI assets as securable objects. You can grant and revoke access to the following AI assets using standard Unity Catalog privileges:^[ai-governance-databricks-on-aws.md]

- **Models**: Registered ML models in Unity Catalog. See MLflow Models for lifecycle management.
- **Functions**: Unity Catalog functions used as agent tools or for data transformations. See Unity Catalog Functions for creating AI agent tools.
- **Connections**: Unity Catalog HTTP connections used to access external APIs and MCP servers. See HTTP Connections for query federation.
- **Hosted foundation models**: Databricks-hosted foundation models available through Foundation Model APIs. See [Foundation Model APIs](/concepts/foundation-model-apis.md) for Unity Catalog permissions.

## AI Traffic Governance with Unity AI Gateway

> **Beta**: This feature is in Beta. Account admins can control access to this feature from the account console **Previews** page. See Manage Databricks Previews.

[Unity AI Gateway](/concepts/unity-ai-gateway.md) is the enterprise control plane for governing AI traffic across your organization. Use Unity AI Gateway to manage and monitor LLM endpoints and MCP servers from a central location:^[ai-governance-databricks-on-aws.md]

- **LLMs**: Control access to hosted and external LLM endpoints, enforce rate limits, and track usage and costs across providers.
- **MCPs**: Manage access to managed, external, and custom MCP servers alongside your LLM endpoints.

## Key Capabilities

AI governance with Unity Catalog provides:^[ai-governance-databricks-on-aws.md]

- **Unified access control**: Apply the same privilege model used for data assets to AI assets like models, functions, and connections.
- **Centralized management**: Govern both AI assets and AI traffic from a single platform.
- **Audit and lineage**: Track access and usage of AI resources with the same audit capabilities as data assets.
- **Scalable governance**: Manage AI resources across the organization with consistent policies.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The unified governance layer for data and AI assets
- [Unity AI Gateway](/concepts/unity-ai-gateway.md) — The control plane for governing AI traffic
- MLflow Models — Registered ML models managed as Unity Catalog securable objects
- Unity Catalog Functions — Functions used as agent tools
- HTTP Connections — Connections for accessing external APIs
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Databricks-hosted foundation model endpoints
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Attribute-based access control for models
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Tag-driven access control for AI and data assets

## Sources

- ai-governance-databricks-on-aws.md

# Citations

1. [ai-governance-databricks-on-aws.md](/references/ai-governance-databricks-on-aws-e6fd4910.md)

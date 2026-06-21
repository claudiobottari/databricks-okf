---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2760d25e5d2cd89c40c8b4d57666dd3c313e2003b1aefd8867d05c2b405e8e84
  pageDirectory: concepts
  sources:
    - ai-governance-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-ai-asset-model
    - UCAAM
    - Unity Catalog object model
  citations:
    - file: ai-governance-databricks-on-aws.md
title: Unity Catalog AI asset model
description: AI assets (models, functions, connections, hosted foundation models) managed as securable objects in Unity Catalog with standard grant/revoke privileges.
tags:
  - unity-catalog
  - ai-governance
  - access-control
  - databricks
timestamp: "2026-06-18T10:42:02.773Z"
---

# Unity Catalog AI asset model

**Unity Catalog AI asset model** extends the data governance capabilities of [Unity Catalog](/concepts/unity-catalog.md) to AI resources, treating AI assets as first-class securable objects that can be managed with the same access control, lineage, and audit model used for data assets.^[ai-governance-databricks-on-aws.md]

## AI assets managed by Unity Catalog

Unity Catalog manages the following AI assets as securable objects. You can grant and revoke access to each using standard Unity Catalog privileges.^[ai-governance-databricks-on-aws.md]

### Models

Registered ML models in Unity Catalog are governed as securable objects. This includes both customer-registered MLflow Models and Databricks-hosted foundation models available through the Foundation Model APIs. See [Manage model lifecycle](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/).^[ai-governance-databricks-on-aws.md]

### Functions

Unity Catalog Functions can be used as agent tools or for data transformations. They are managed as securable objects, allowing fine-grained access control for AI agent usage. See [Create AI agent tools using Unity Catalog functions](https://docs.databricks.com/aws/en/generative-ai/agent-framework/create-custom-tool).^[ai-governance-databricks-on-aws.md]

### Connections

HTTP Connections in Unity Catalog are used to access external APIs and MCP (Model Context Protocol) servers. These connections are securable objects that can be granted and revoked like other assets. See [HTTP connections](https://docs.databricks.com/aws/en/query-federation/http).^[ai-governance-databricks-on-aws.md]

### Hosted foundation models

Databricks-hosted foundation models available through Foundation Model APIs are managed as Unity Catalog securable objects with their own permission model. See [Foundation model Unity Catalog permissions](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/model-uc-permissions).^[ai-governance-databricks-on-aws.md]

## Governance capabilities

The AI asset model provides the same governance capabilities that Unity Catalog offers for data assets:^[ai-governance-databricks-on-aws.md]

- **Unified access control**: Apply the same privilege model used for data assets to AI assets like models, functions, and connections.
- **Centralized management**: Govern both AI assets and AI traffic (through [Unity AI Gateway](/concepts/unity-ai-gateway.md)) from a single platform.
- **Audit and lineage**: Track access and usage of AI resources with the same audit capabilities as data assets.
- **Scalable governance**: Manage AI resources across the organization with consistent policies.

## Related concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The unified governance layer for data and AI assets
- [AI Governance with Unity Catalog](/concepts/ai-governance-with-unity-catalog.md) — Broader governance covering AI assets and AI traffic
- [Unity AI Gateway](/concepts/unity-ai-gateway.md) — The control plane for governing AI traffic
- MLflow Models — Registered ML models managed as Unity Catalog securable objects
- Unity Catalog Functions — Functions used as agent tools
- HTTP Connections — Connections for accessing external APIs and MCP servers
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Databricks-hosted foundation model endpoints
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Attribute-based access control for models (Beta)
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Tag-driven access control for AI and data assets

## Sources

- ai-governance-databricks-on-aws.md

# Citations

1. [ai-governance-databricks-on-aws.md](/references/ai-governance-databricks-on-aws-e6fd4910.md)

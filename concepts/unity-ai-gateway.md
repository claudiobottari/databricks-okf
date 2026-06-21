---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 01ae749d535c5fa0d077258d3f8e1fe71f183b41de3db752463eaa2a7485a180
  pageDirectory: concepts
  sources:
    - ai-governance-databricks-on-aws.md
    - get-started-with-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - unity-ai-gateway
    - UAG
  citations:
    - file: ai-governance-databricks-on-aws.md
    - file: get-started-with-unity-catalog-databricks-on-aws.md
title: Unity AI Gateway
description: An enterprise control plane for governing AI traffic across an organization, managing and monitoring LLM endpoints and MCP servers centrally.
tags:
  - ai-gateway
  - ai-traffic
  - governance
  - databricks
timestamp: "2026-06-19T22:01:01.389Z"
---

# Unity AI Gateway

**Unity AI Gateway** is the enterprise control plane for governing AI traffic across an organization, extending [Unity Catalog](/concepts/unity-catalog.md) governance to AI resources. It provides centralized management and monitoring of LLM endpoints, agents, and MCP servers, enabling access control, audit logging, and observability across all AI interactions from a unified UI. ^[ai-governance-databricks-on-aws.md]

## Overview

Unity AI Gateway is a Beta feature that allows organizations to manage and monitor AI endpoints from a central location. Account admins can control access to this feature from the account console **Previews** page. ^[ai-governance-databricks-on-aws.md]

The gateway serves as the enterprise control plane for governing AI traffic, applying the same governance principles that protect data assets to AI assets and AI traffic. ^[ai-governance-databricks-on-aws.md, get-started-with-unity-catalog-databricks-on-aws.md]

## Key Capabilities

### LLM Endpoint Management

Unity AI Gateway enables organizations to control access to hosted and external LLM endpoints. Administrators can enforce rate limits and track usage and costs across different providers from a single interface. ^[ai-governance-databricks-on-aws.md]

### MCP Server Management

The gateway also provides management capabilities for MCP servers, including managed, external, and custom MCP servers. These can be managed alongside LLM endpoints in the same unified interface. ^[ai-governance-databricks-on-aws.md]

### Agent Governance

Unity AI Gateway extends governance to AI agents, allowing organizations to implement access control, audit logging, and observability for agent interactions. ^[get-started-with-unity-catalog-databricks-on-aws.md]

## Integration with Unity Catalog

Unity AI Gateway is part of the broader [AI Governance with Unity Catalog](/concepts/ai-governance-unity-catalog.md) framework. While Unity Catalog governs AI assets (models, functions, connections, and hosted foundation models) as securable objects with standard privileges, Unity AI Gateway specifically governs AI traffic — the runtime interactions with those AI resources. ^[ai-governance-databricks-on-aws.md]

This integration means organizations can apply the same access control, lineage, and audit model that protects data assets to both AI assets and AI traffic. ^[ai-governance-databricks-on-aws.md]

## Use Cases

- **Centralized AI governance**: Manage all LLM endpoints, agents, and MCP servers from a single control plane.
- **Access control**: Control which users and groups can access specific AI endpoints.
- **Rate limiting**: Enforce usage limits to prevent abuse and manage costs.
- **Cost tracking**: Monitor and track AI usage costs across different providers.
- **Audit logging**: Maintain audit trails for all AI interactions across the organization.

## Related Concepts

- [AI Governance with Unity Catalog](/concepts/ai-governance-unity-catalog.md) — The broader framework for governing AI assets and traffic.
- [Unity Catalog](/concepts/unity-catalog.md) — The unified governance layer for data and AI.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Databricks-hosted foundation models that can be governed through Unity Catalog.
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — Custom and foundation model endpoints that can integrate with Unity AI Gateway.

## Sources

- ai-governance-databricks-on-aws.md
- get-started-with-unity-catalog-databricks-on-aws.md

# Citations

1. [ai-governance-databricks-on-aws.md](/references/ai-governance-databricks-on-aws-e6fd4910.md)
2. [get-started-with-unity-catalog-databricks-on-aws.md](/references/get-started-with-unity-catalog-databricks-on-aws-3c48b4d4.md)

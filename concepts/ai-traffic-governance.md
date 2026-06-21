---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6e80f8ed715e0adc9fad9d89689ea3f03321f272bf664cc7bb0f6e7882900372
  pageDirectory: concepts
  sources:
    - ai-governance-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-traffic-governance
    - ATG
  citations:
    - file: ai-governance-databricks-on-aws.md
title: AI Traffic Governance
description: The practice of controlling access, enforcing rate limits, and tracking usage and costs for LLM endpoints and MCP servers through a central gateway.
tags:
  - ai-traffic
  - governance
  - rate-limiting
  - cost-tracking
timestamp: "2026-06-19T22:01:01.796Z"
---

# AI Traffic Governance

**AI traffic governance** is the practice of controlling, monitoring, and managing how artificial intelligence resources — including large language model (LLM) endpoints and Model Context Protocol (MCP) servers — are invoked and consumed across an organization. It extends the data governance model of [Unity Catalog](/concepts/unity-catalog.md) to cover runtime AI usage, providing enterprises with centralized control over access, rate limits, usage tracking, and cost monitoring. ^[ai-governance-databricks-on-aws.md]

## Overview

AI traffic governance is a core capability of [Unity AI Gateway](/concepts/unity-ai-gateway.md), which serves as the enterprise control plane for all AI inference traffic. While AI Asset Governance with Unity Catalog handles who can register, deploy, or modify AI assets, AI traffic governance controls how those assets are used at runtime — who can invoke them, how frequently they can be called, and how that usage is tracked and governed. ^[ai-governance-databricks-on-aws.md]

Unity AI Gateway is currently in **Beta**. Account admins can enable or disable access to this feature from the account console **Previews** page. ^[ai-governance-databricks-on-aws.md]

## Capabilities

Unity AI Gateway provides the following governance capabilities for AI traffic: ^[ai-governance-databricks-on-aws.md]

### LLM Management

- **Access control**: Control which users, groups, or service principals can invoke hosted and external LLM endpoints.
- **Rate limiting**: Enforce rate limits on API calls to prevent abuse, control costs, and ensure fair usage across consumers.
- **Usage tracking**: Track usage and costs across different LLM providers from a centralized location.
- **Provider aggregation**: Manage multiple LLM providers (e.g., Databricks-hosted foundation models, third-party APIs like OpenAI or Anthropic) through a single gateway.

### MCP Server Management

- **Unified management**: Manage access to managed, external, and custom MCP servers alongside LLM endpoints.
- **Access control**: Govern which principals can reach which MCP servers.

## Relationship to AI Asset Governance

AI traffic governance complements AI Asset Governance with Unity Catalog. The two layers address different aspects of AI governance: ^[ai-governance-databricks-on-aws.md]

| Governance Layer | Focus | Mechanism |
|-----------------|-------|-----------|
| AI Asset Governance | Who can register, deploy, and manage AI assets | Unity Catalog privileges (e.g., `EXECUTE`, `CREATE MODEL`, `USAGE`) |
| AI Traffic Governance | How AI assets are invoked and consumed at runtime | Unity AI Gateway (rate limits, usage tracking, access control) |

Unity Catalog manages AI assets as securable objects — including models, functions, connections, and hosted foundation models — using standard Unity Catalog privileges. Unity AI Gateway then governs the runtime traffic to those assets, providing operational controls that asset-level permissions alone cannot enforce. ^[ai-governance-databricks-on-aws.md]

## Use Cases

### Cost Control and Budget Management

Organizations can use AI traffic governance to set rate limits and track costs across teams, projects, or individual users. This prevents runaway spending from uncontrolled LLM API calls and enables chargeback or showback reporting. ^[ai-governance-databricks-on-aws.md]

### Security and Compliance

By centralizing access control for all AI inference endpoints, AI traffic governance reduces the risk of unauthorized model access, data exfiltration through model invocation, and compliance violations. MCP servers can be governed with the same level of control as LLM endpoints. ^[ai-governance-databricks-on-aws.md]

### Operational Visibility

Usage tracking across all providers gives administrators a single pane of glass for understanding how AI resources are consumed across the organization. This supports capacity planning, provider optimization, and anomaly detection. ^[ai-governance-databricks-on-aws.md]

## Related Concepts

- [Unity AI Gateway](/concepts/unity-ai-gateway.md) — The enterprise control plane providing AI traffic governance capabilities
- [Unity Catalog](/concepts/unity-catalog.md) — The data and AI governance platform providing the foundation for asset governance
- AI Asset Governance with Unity Catalog — Governance of AI resources as securable objects using Unity Catalog privileges
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Databricks-hosted AI models that can be governed through AI traffic governance
- [MCP Servers](/concepts/mlflow-mcp-server.md) — Model Context Protocol servers that can be managed alongside LLM endpoints
- Rate Limiting — Enforcing maximum request rates per consumer
- Usage Monitoring — Tracking and reporting on AI resource consumption

## Sources

- ai-governance-databricks-on-aws.md

# Citations

1. [ai-governance-databricks-on-aws.md](/references/ai-governance-databricks-on-aws-e6fd4910.md)

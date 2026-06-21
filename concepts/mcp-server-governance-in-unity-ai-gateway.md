---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9af6bc3d28f7a56e27517f50c46a022faddd9cce6528c0d88f3235e623219538
  pageDirectory: concepts
  sources:
    - ai-governance-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mcp-server-governance-in-unity-ai-gateway
    - MSGIUAG
  citations:
    - file: ai-governance-databricks-on-aws.md
title: MCP server governance in Unity AI Gateway
description: Management of access to managed, external, and custom MCP (Model Context Protocol) servers alongside LLM endpoints through Unity AI Gateway.
tags:
  - mcp
  - ai-gateway
  - server-management
timestamp: "2026-06-18T14:21:00.117Z"
---

# MCP Server Governance in Unity AI Gateway

**MCP server governance** in [Unity AI Gateway](/concepts/unity-ai-gateway.md) refers to the centralized control of access, monitoring, and management of [MCP servers](/concepts/mlflow-mcp-server.md) (Model Context Protocol servers) alongside LLM endpoints across an organization. Governance is part of the broader [AI Governance](/concepts/ai-governance.md) framework provided by [Unity Catalog](/concepts/unity-catalog.md), extending data governance principles to AI traffic.

## Overview

Unity AI Gateway is the enterprise control plane for governing AI traffic across your organization. It enables administrators to manage and monitor both LLM endpoints and MCP servers from a single location. For MCP servers, governance includes controlling access to managed, external, and custom MCP servers alongside LLM endpoints. ^[ai-governance-databricks-on-aws.md]

## Key Governance Capabilities

Unity AI Gateway provides the following governance capabilities for MCP servers:

- **Centralized management**: Manage all MCP servers (managed, external, custom) alongside LLM endpoints in one place.
- **Access control**: Control which users, service principals, or groups can invoke or administer MCP servers.
- **Rate limiting and usage tracking**: Enforce rate limits and track usage and costs, similar to LLM endpoints.
- **Monitoring**: Observe traffic patterns and audit access to MCP servers.

These capabilities mirror the governance features available for LLM endpoints, as MCP servers are treated as first-class governed resources within the AI Gateway. ^[ai-governance-databricks-on-aws.md]

## Integration with Unity Catalog

MCP server governance builds on Unity Catalog's AI asset governance model. [Unity Catalog](/concepts/unity-catalog.md) already manages AI assets as securable objects, including:

- **Models**: Registered ML models
- **Functions**: Unity Catalog functions used as agent tools
- **Connections**: HTTP connections used to access external APIs and MCP servers

Connections are particularly relevant for MCP server governance, as external and custom MCP servers are typically accessed through Unity Catalog HTTP connections. This means the same access control, lineage, and audit mechanisms that protect data assets apply to MCP server interactions. ^[ai-governance-databricks-on-aws.md]

## How to Govern MCP Servers

Governance is configured through the Unity AI Gateway interface (available in Beta). Administrators can:

1. Register managed, external, or custom MCP servers in the gateway.
2. Define access policies using Unity Catalog privileges (e.g., `EXECUTE` on connections or MCP server endpoints).
3. Set rate limits and budget policies to control usage.
4. Monitor invocation logs and cost metrics through the gateway dashboard.

The exact steps depend on the type of MCP server (managed, external, or custom) and the desired governance rules. See [Unity AI Gateway](/concepts/unity-ai-gateway.md) for detailed configuration instructions. ^[ai-governance-databricks-on-aws.md]

## Related Concepts

- [Unity AI Gateway](/concepts/unity-ai-gateway.md) — The enterprise control plane for AI traffic governance
- [Unity Catalog](/concepts/unity-catalog.md) — Data and AI governance platform providing access control, lineage, and audit
- [MCP Servers](/concepts/mlflow-mcp-server.md) — Model Context Protocol servers providing tool-calling capabilities
- HTTP Connections — Unity Catalog securable objects used to access external MCP servers
- [AI Governance](/concepts/ai-governance.md) — The overarching framework for governing AI resources
- [LLM endpoint governance](/concepts/llm-endpoint-governance.md) — Governance of hosted and external LLM endpoints in Unity AI Gateway

## Sources

- ai-governance-databricks-on-aws.md

# Citations

1. [ai-governance-databricks-on-aws.md](/references/ai-governance-databricks-on-aws-e6fd4910.md)

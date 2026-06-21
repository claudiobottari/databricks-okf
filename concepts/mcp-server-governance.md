---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 236bb714dfa1f204d58f3e30509152ecad6cfcfe5f00ed87c0f6d5872a639ff9
  pageDirectory: concepts
  sources:
    - ai-governance-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mcp-server-governance
    - MSG
    - mcp-server-governance-in-unity-ai-gateway
    - MSGIUAG
  citations:
    - file: ai-governance-databricks-on-aws.md
title: MCP Server Governance
description: Managing access to managed, external, and custom MCP (Model Context Protocol) servers alongside LLM endpoints through the Unity AI Gateway.
tags:
  - MCP
  - governance
  - AI-gateway
timestamp: "2026-06-19T17:29:50.565Z"
---

# MCP Server Governance

**MCP Server Governance** refers to the management and control of [MCP servers](/concepts/mlflow-mcp-server.md) within an organization's AI infrastructure, using [Unity Catalog](/concepts/unity-catalog.md) and [Unity AI Gateway](/concepts/unity-ai-gateway.md) to enforce access control, monitor usage, and apply consistent policies across managed, external, and custom MCP servers.

## Overview

MCP servers are governed as part of an organization's AI traffic alongside LLM endpoints. Unity AI Gateway provides the enterprise control plane for managing and monitoring MCP servers from a central location, applying the same governance model used for other AI resources.^[ai-governance-databricks-on-aws.md]

## Governance Capabilities

### Access Control

MCP servers are managed as securable objects within Unity Catalog. Access to MCP servers can be granted and revoked using standard Unity Catalog privileges, consistent with the access control model applied to other AI assets such as models, functions, and connections.^[ai-governance-databricks-on-aws.md]

### Centralized Management

Unity AI Gateway enables organizations to manage access to managed, external, and custom MCP servers alongside their LLM endpoints from a single location. This centralized approach allows governance teams to apply consistent policies across all AI traffic.^[ai-governance-databricks-on-aws.md]

### Monitoring and Usage Tracking

Through Unity AI Gateway, organizations can track usage and enforce rate limits on MCP servers, providing visibility into how these AI resources are being consumed across the organization.^[ai-governance-databricks-on-aws.md]

## MCP Server Types

Unity AI Gateway supports governing multiple types of MCP servers:

- **Managed MCP servers**: Servers hosted and managed within the Databricks environment
- **External MCP servers**: Third-party or externally hosted MCP servers accessed through HTTP Connections
- **Custom MCP servers**: Organization-specific MCP server implementations

All types are governed through the same centralized control plane.^[ai-governance-databricks-on-aws.md]

## Integration with Unity Catalog

MCP server governance integrates with Unity Catalog's broader AI governance framework, which applies the same access control, lineage, and audit model used for data assets to AI resources. This unified approach ensures consistent governance across data and AI assets.^[ai-governance-databricks-on-aws.md]

## Related Concepts

- [Unity AI Gateway](/concepts/unity-ai-gateway.md) — The enterprise control plane for governing AI traffic
- [Unity Catalog](/concepts/unity-catalog.md) — The unified governance layer for data and AI assets
- [AI Governance with Unity Catalog](/concepts/ai-governance-unity-catalog.md) — The broader framework for governing AI resources
- HTTP Connections — Connections used to access external APIs and MCP servers
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Attribute-based access control for AI assets
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Tag-driven access control for AI and data assets

## Sources

- ai-governance-databricks-on-aws.md

# Citations

1. [ai-governance-databricks-on-aws.md](/references/ai-governance-databricks-on-aws-e6fd4910.md)

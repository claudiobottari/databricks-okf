---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 63db59d847a4ef96eda9bd0891937dfcb5c80c86e352b0dd4b26b5a326e43bbc
  pageDirectory: concepts
  sources:
    - get-started-with-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-governance-with-unity-ai-gateway
    - AGWUAG
  citations:
    - file: get-started-with-unity-catalog-databricks-on-aws.md
title: AI Governance with Unity AI Gateway
description: Extension of Unity Catalog governance to AI, providing enterprise governance for LLM endpoints, agents, and MCP servers
tags:
  - ai-governance
  - llm
  - gateway
timestamp: "2026-06-19T10:45:44.237Z"
---

## AI Governance with Unity AI Gateway

**AI Governance with Unity AI Gateway** extends the governance capabilities of [Unity Catalog](/concepts/unity-catalog.md) to artificial intelligence workloads. It provides a unified control plane for managing, securing, and monitoring AI interactions — including LLM endpoints, agents, and MCP servers — across the Databricks platform. ^[get-started-with-unity-catalog-databricks-on-aws.md]

### Overview

Unity AI Gateway is a feature of Unity Catalog that brings the same governance principles used for data (access control, lineage, auditing, and discovery) to AI assets. It allows organizations to implement enterprise‑grade governance for all AI interactions through a single, unified UI. ^[get-started-with-unity-catalog-databricks-on-aws.md]

### Key Capabilities

- **Access control**: Define who can call which models, agents, or MCP servers, and under what conditions.
- **Audit logging**: Record every AI interaction for compliance and security investigations.
- **Observability**: Monitor usage, latency, errors, and costs for all AI endpoints in one place.
- **Unified UI**: Manage AI governance policies alongside data governance policies in the same Unity Catalog interface.

These capabilities enable organizations to enforce consistent security and compliance policies across both data and AI workflows. ^[get-started-with-unity-catalog-databricks-on-aws.md]

### Relationship to Unity Catalog

Unity AI Gateway is an extension of Unity Catalog’s governance layer. Just as Unity Catalog provides a single place to manage access to tables, files, and models, Unity AI Gateway extends that same paradigm to LLM endpoints, agents, and [MCP servers](/concepts/mlflow-mcp-server.md). This unification means that governance policies — such as who can use a particular model or which data sources an agent can access — can be defined and audited in a consistent manner. ^[get-started-with-unity-catalog-databricks-on-aws.md]

### Getting Started

For detailed setup instructions and a complete overview of Unity AI Gateway capabilities, refer to the official documentation: [Unity AI Gateway](https://docs.databricks.com/aws/en/ai-gateway/). ^[get-started-with-unity-catalog-databricks-on-aws.md]

### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The unified governance layer for data and AI on Databricks.
- [LLM endpoints](/concepts/model-serving-endpoint.md) – Managed serving endpoints for large language models.
- Agents – AI assistants that use LLMs and tools to perform tasks.
- [MCP servers](/concepts/mlflow-mcp-server.md) – Model Context Protocol servers for tool integration.
- [Attribute-based access control](/concepts/attribute-based-access-control-abac.md) – Dynamic access policies used in Unity Catalog.
- [Audit logging](/concepts/abac-policy-audit-logging.md) – Recording of actions for compliance and security.
- Observability – Monitoring and tracking of system performance and usage.

### Sources

- get-started-with-unity-catalog-databricks-on-aws.md

# Citations

1. [get-started-with-unity-catalog-databricks-on-aws.md](/references/get-started-with-unity-catalog-databricks-on-aws-3c48b4d4.md)

---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 56993d8a4823589d9c19435e8b75f45a9fafbcd2f9198b5b6f7b7e0415c563c3
  pageDirectory: concepts
  sources:
    - ai-governance-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-assets-as-securable-objects
    - AAASO
  citations:
    - file: ai-governance-databricks-on-aws.md
title: AI Assets as Securable Objects
description: AI resources (models, functions, connections, hosted foundation models) managed as securable objects in Unity Catalog with standard privileges for grant and revoke operations.
tags:
  - unity-catalog
  - access-control
  - ai-governance
  - databricks
timestamp: "2026-06-19T22:01:28.129Z"
---

# AI Assets as Securable Objects

**AI Assets as Securable Objects** refers to the framework within Unity Catalog that treats AI resources—such as models, functions, and other AI components—as securable objects with the same access control, lineage tracking, and audit capabilities as traditional data assets. This approach extends data governance to AI assets, enabling standardized permission management across the AI lifecycle.

## Overview

Unity Catalog manages AI assets as securable objects, meaning they can be protected and tracked under the same governance framework as your organization's data. This allows you to grant and revoke access to AI resources using standard Unity Catalog privileges, providing a unified approach to governing both data and AI.^[ai-governance-databricks-on-aws.md]

## AI Assets Governed as Securable Objects

Unity Catalog governs the following AI assets as securable objects:

### Models
Registered ML models in Unity Catalog are managed as securable objects. You can control access to these models throughout their lifecycle, from development through deployment. See Manage model lifecycle.^[ai-governance-databricks-on-aws.md]

### Functions
Unity Catalog functions used as agent tools or for data transformations are securable objects. These can include custom functions that serve as tools for AI agents or perform data processing operations. See Create AI agent tools using Unity Catalog functions.^[ai-governance-databricks-on-aws.md]

### Connections
Unity Catalog HTTP connections used to access external APIs and MCP servers are securable objects. These connections enable AI systems to interact with external services while maintaining governance. See HTTP connections.^[ai-governance-databricks-on-aws.md]

### Hosted Foundation Models
Databricks-hosted foundation models available through Foundation Model APIs are governed as securable objects. Access to these models is controlled through Unity Catalog permissions. See [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md).^[ai-governance-databricks-on-aws.md]

## AI Traffic Governance

In addition to managing AI assets as securable objects, Unity AI Gateway provides a separate control plane for governing AI traffic across the organization. This includes:

- **LLMs**: Controlling access to hosted and external LLM endpoints, enforcing rate limits, and tracking usage and costs across providers
- **MCPs**: Managing access to managed, external, and custom MCP servers alongside LLM endpoints

See [Unity AI Gateway](/concepts/unity-ai-gateway.md).^[ai-governance-databricks-on-aws.md]

## Benefits

Managing AI assets as securable objects provides several advantages:

- **Unified governance**: Apply the same access control model to both data and AI assets
- **Standardized permissions**: Use consistent privilege management across all AI resources
- **Audit capabilities**: Track access and usage of AI assets through existing audit mechanisms
- **Lineage tracking**: Maintain visibility into how AI assets are used and modified

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- Securable objects - The underlying framework for governance
- [AI Governance](/concepts/ai-governance.md)
- Model lifecycle management
- Agent tools

## Sources

- ai-governance-databricks-on-aws.md

# Citations

1. [ai-governance-databricks-on-aws.md](/references/ai-governance-databricks-on-aws-e6fd4910.md)

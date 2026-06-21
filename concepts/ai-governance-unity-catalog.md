---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fc5d6abe4d86602e53de4c080271d2328937e0fc29278019bc5bd79e5b29dda5
  pageDirectory: concepts
  sources:
    - ai-governance-databricks-on-aws.md
    - what-is-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - ai-governance-unity-catalog
    - AG(C
    - Data Governance in Unity Catalog
    - Governance in Unity Catalog
    - Migration of system tags to governance in Unity Catalog
  citations:
    - file: ai-governance-databricks-on-aws.md
    - file: what-is-unity-catalog-databricks-on-aws.md
title: AI Governance (Unity Catalog)
description: Extension of Unity Catalog's data governance capabilities to AI assets, applying access control, lineage, and audit models to AI resources.
tags:
  - ai-governance
  - unity-catalog
  - data-governance
  - databricks
timestamp: "2026-06-19T22:00:52.611Z"
---

# AI Governance (Unity Catalog)

**AI Governance** within [Unity Catalog](/concepts/unity-catalog.md) extends the same data governance capabilities—access control, lineage, and auditing—to AI resources. This unified approach ensures that AI assets (models, functions, connections) and AI traffic (LLM endpoint usage, MCP server calls) are governed with the same policies and protections that apply to data assets. ^[ai-governance-databricks-on-aws.md, what-is-unity-catalog-databricks-on-aws.md]

## AI Asset Governance

Unity Catalog treats AI assets as securable objects, allowing administrators to grant and revoke access using standard Unity Catalog privileges. The following AI assets are managed directly within the catalog: ^[ai-governance-databricks-on-aws.md]

- **Models**: Registered ML models stored in Unity Catalog. Access controls apply to the model object, enabling fine-grained permissions on model versions and stages. ^[ai-governance-databricks-on-aws.md]
- **Functions**: Unity Catalog functions used as agent tools or for data transformations. These can be shared across workspaces and governed like any other securable object. ^[ai-governance-databricks-on-aws.md]
- **Connections**: Unity Catalog HTTP connections used to access external APIs and MCP servers. These allow governed access to external services. ^[ai-governance-databricks-on-aws.md]
- **Hosted foundation models**: Databricks-hosted foundation models available through Foundation Model APIs, each governed by Unity Catalog permissions. ^[ai-governance-databricks-on-aws.md]

All AI assets benefit from Unity Catalog's built-in tracking of **data lineage**, **audit logging**, and **data classification** — the same infrastructure that protects tables and volumes. ^[what-is-unity-catalog-databricks-on-aws.md]

## AI Traffic Governance with Unity AI Gateway

**Unity AI Gateway** provides a centralized enterprise control plane for governing AI traffic across the organization. It is currently in Beta and can be enabled by account admins from the **Previews** page in the account console. ^[ai-governance-databricks-on-aws.md]

Key capabilities include: ^[ai-governance-databricks-on-aws.md]

| Capability | Description |
|------------|-------------|
| **LLM endpoints** | Control access to hosted and external LLM endpoints, enforce rate limits, and track usage and costs across providers. |
| **MCP servers** | Manage access to managed, external, and custom MCP servers alongside LLM endpoints from a single interface. |

Unity AI Gateway allows administrators to monitor, route, and enforce policies on AI traffic in real time, extending Unity Catalog's governance model to the inference layer. ^[ai-governance-databricks-on-aws.md]

## Benefits of Unified Governance

Because AI governance is built on the same foundation as data governance, organizations can: ^[ai-governance-databricks-on-aws.md, what-is-unity-catalog-databricks-on-aws.md]

- Apply consistent **access control** policies across both data and AI assets using the same privilege model.
- Track **lineage** for models and functions as data moves through pipelines.
- Maintain a complete **audit trail** of all AI resource access through audit log system tables.
- Use **Catalog Explorer** to discover, browse, and manage both data and AI securable objects in a single interface.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Unity AI Gateway](/concepts/unity-ai-gateway.md)
- Access Control in Unity Catalog
- [Data Lineage](/concepts/data-lineage.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md)

## Sources

- ai-governance-databricks-on-aws.md
- what-is-unity-catalog-databricks-on-aws.md

# Citations

1. [ai-governance-databricks-on-aws.md](/references/ai-governance-databricks-on-aws-e6fd4910.md)
2. [what-is-unity-catalog-databricks-on-aws.md](/references/what-is-unity-catalog-databricks-on-aws-ea58b0e9.md)

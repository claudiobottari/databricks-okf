---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2a74dd9fd20ad26e4aead553944d0568a8a1fe0f7a0f073b541a4a3cd799afa1
  pageDirectory: concepts
  sources:
    - ai-governance-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-ai-asset-governance
    - UCAAG
  citations:
    - file: ai-governance-databricks-on-aws.md
title: Unity Catalog AI Asset Governance
description: Managing AI assets—models, functions, connections, and hosted foundation models—as securable objects with standard Unity Catalog privileges.
tags:
  - unity-catalog
  - governance
  - AI-assets
timestamp: "2026-06-19T17:29:29.668Z"
---

---

title: Unity Catalog AI Asset Governance
summary: Extends Unity Catalog data governance to AI resources—models, functions, connections, and hosted foundation models—with standard access control, lineage, and audit. Also covers AI traffic governance via Unity AI Gateway (Beta).
sources:
  - ai-governance-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T13:55:18.032Z"
updatedAt: "2026-06-19T13:55:18.032Z"
tags:
  - unity-catalog
  - ai-governance
  - access-control
  - ai-gateway
aliases:
  - unity-catalog-ai-asset-governance
  - UC-AI-governance
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

## Unity Catalog AI Asset Governance

**Unity Catalog AI Asset Governance** extends the data governance model of [Unity Catalog](/concepts/unity-catalog.md) to AI resources, applying the same access control, lineage, and audit capabilities that protect data assets to AI assets and AI traffic. ^[ai-governance-databricks-on-aws.md]

---

### AI Asset Governance with Unity Catalog

Unity Catalog manages AI assets as securable objects. Administrators can grant and revoke access to the following AI asset types using standard [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md):

- **Models**: Registered ML models stored in Unity Catalog. See [Unity Catalog Model Registry](/concepts/unity-catalog-model-registry.md). ^[ai-governance-databricks-on-aws.md]
- **Functions**: Unity Catalog functions used as agent tools or for data transformations. See Create AI agent tools using Unity Catalog functions. ^[ai-governance-databricks-on-aws.md]
- **Connections**: Unity Catalog HTTP connections used to access external APIs and MCP servers. See HTTP connections. ^[ai-governance-databricks-on-aws.md]
- **Hosted foundation models**: Databricks-hosted foundation models available through the Foundation Model APIs. See [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md). ^[ai-governance-databricks-on-aws.md]

---

### AI Traffic Governance with Unity AI Gateway (Beta)

**Unity AI Gateway** is the enterprise control plane for governing AI traffic across an organization. It is currently in Beta release. ^[ai-governance-databricks-on-aws.md]

Use Unity AI Gateway to manage and monitor LLM endpoints and MCP servers from a central location:

- **LLMs**: Control access to hosted and external LLM endpoints, enforce rate limits, and track usage and costs across providers. ^[ai-governance-databricks-on-aws.md]
- **MCPs**: Manage access to managed, external, and custom MCP servers alongside LLM endpoints. ^[ai-governance-databricks-on-aws.md]

Account admins can control access to this feature from the account console **Previews** page. See Manage Databricks previews. ^[ai-governance-databricks-on-aws.md]

For complete documentation, refer to [Unity AI Gateway](/concepts/unity-ai-gateway.md). ^[ai-governance-databricks-on-aws.md]

---

### Sources

- ai-governance-databricks-on-aws.md

# Citations

1. [ai-governance-databricks-on-aws.md](/references/ai-governance-databricks-on-aws-e6fd4910.md)

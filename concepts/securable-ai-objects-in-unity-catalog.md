---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 579a899b656508db04465935bc4c8a720038cbb0e7284d186dfbb0bed485b06c
  pageDirectory: concepts
  sources:
    - ai-governance-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - securable-ai-objects-in-unity-catalog
    - SAOIUC
  citations:
    - file: ai-governance-databricks-on-aws.md
title: Securable AI Objects in Unity Catalog
description: AI resources—including models, functions, HTTP connections, and hosted foundation models—that can have permissions granted and revoked using standard Unity Catalog privileges.
tags:
  - unity-catalog
  - security
  - permissions
timestamp: "2026-06-19T17:29:19.216Z"
---

Here is the wiki page for "Securable AI Objects in Unity Catalog", written based solely on the provided source material.

---

## Securable AI Objects in Unity Catalog

**Securable AI Objects in Unity Catalog** are AI assets that Unity Catalog manages alongside traditional data assets, applying the same access control, lineage, and audit models to protect them. This capability is part of [AI Governance on Databricks](/concepts/ai-governance-on-databricks.md) and extends Unity Catalog's governance framework to AI resources. ^[ai-governance-databricks-on-aws.md]

### Overview

Databricks AI governance extends the data governance capabilities of Unity Catalog to AI resources. This means that AI assets benefit from the same access control, lineage tracking, and audit model that protects data assets. ^[ai-governance-databricks-on-aws.md]

Unity Catalog manages AI assets as securable objects. This allows administrators to grant and revoke access to these assets using standard Unity Catalog privileges. ^[ai-governance-databricks-on-aws.md]

### Types of Securable AI Objects

The following AI assets are managed as securable objects in Unity Catalog:

- **Models**: Registered ML models in Unity Catalog. See [Manage Model Lifecycle](/concepts/ml-lifecycle.md) for details. ^[ai-governance-databricks-on-aws.md]
- **Functions**: Unity Catalog functions used as agent tools or for data transformations. See Create AI Agent Tools Using Unity Catalog Functions for details. ^[ai-governance-databricks-on-aws.md]
- **Connections**: Unity Catalog HTTP connections used to access external APIs and MCP servers. See HTTP Connections for details. ^[ai-governance-databricks-on-aws.md]
- **Hosted foundation models**: Databricks-hosted foundation models available through Foundation Model APIs. See [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md) for details. ^[ai-governance-databricks-on-aws.md]

### Governance Model

Each securable AI object inherits the same governance model as other Unity Catalog objects. Standard [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — such as `SELECT`, `USAGE`, `MODIFY`, and `OWNERSHIP` — can be granted and revoked on these AI assets, ensuring that only authorized users, service principals, and groups can access or modify them. ^[ai-governance-databricks-on-aws.md]

### Related Concepts

- [AI Governance on Databricks](/concepts/ai-governance-on-databricks.md)
- [Unity AI Gateway](/concepts/unity-ai-gateway.md) — The enterprise control plane for governing AI traffic, including LLM endpoints and MCP servers.
- [Unity Catalog](/concepts/unity-catalog.md)
- [Manage Model Lifecycle](/concepts/ml-lifecycle.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md)

### Sources

- ai-governance-databricks-on-aws.md

# Citations

1. [ai-governance-databricks-on-aws.md](/references/ai-governance-databricks-on-aws-e6fd4910.md)

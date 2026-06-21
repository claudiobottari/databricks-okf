---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d3f6c8df69b7ed1bf1103889863e2f0b8b98d6ea216ac19dc941cd8ecc1d1c31
  pageDirectory: concepts
  sources:
    - ai-governance-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - securable-ai-assets-in-unity-catalog
    - SAAIUC
  citations:
    - file: ai-governance-databricks-on-aws.md
title: Securable AI Assets in Unity Catalog
description: ML models, Unity Catalog functions, HTTP connections, and hosted foundation models managed as securable objects with grant/revoke privileges.
tags:
  - unity-catalog
  - securable-objects
  - ml-models
  - functions
timestamp: "2026-06-19T13:55:37.301Z"
---

# Securable AI Assets in Unity Catalog

**Securable AI Assets in Unity Catalog** are AI resources that Unity Catalog manages as securable objects, extending the same data governance model—access control, lineage, and auditing—to AI assets. Administrators can grant and revoke privileges on these assets using standard Unity Catalog permissions. ^[ai-governance-databricks-on-aws.md]

## Overview

Unity Catalog treats AI assets as first-class securable objects, applying the same governance framework that protects data assets to AI resources. This enables organizations to enforce consistent access control policies across both data and AI assets within a single governance platform. ^[ai-governance-databricks-on-aws.md]

## List of Securable AI Assets

### Models

Registered ML models stored in Unity Catalog. Access to read, update, or execute a model is controlled through privileges such as `EXECUTE`, `READ`, and `WRITE`. See Manage model lifecycle. ^[ai-governance-databricks-on-aws.md]

### Functions

Unity Catalog functions used as tools by AI agents or for data transformations. These functions can be granted access just like any other securable object. See Create AI agent tools using Unity Catalog functions. ^[ai-governance-databricks-on-aws.md]

### Connections

HTTP connections created in Unity Catalog to access external APIs or [MCP servers](/concepts/mlflow-mcp-server.md). These are securable objects that control which principals can use the connection. See HTTP connections. ^[ai-governance-databricks-on-aws.md]

### Hosted Foundation Models

Databricks-hosted foundation models available through the Foundation Model APIs. Unity Catalog governs access to these models using standard privileges, allowing administrators to control which users or service principals can invoke them. See [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md). ^[ai-governance-databricks-on-aws.md]

## Governance Model

Unity Catalog applies the following governance capabilities to AI assets:

- **Access control**: Grant and revoke privileges using standard Unity Catalog permissions
- **Lineage tracking**: Track how AI assets are used and transformed across workflows
- **Audit logging**: Record all access and operations on AI assets for compliance

This unified governance model ensures that AI assets receive the same level of protection as traditional data assets. ^[ai-governance-databricks-on-aws.md]

## Related Governance Capabilities

### AI Traffic Governance (Beta)

Beyond asset-level governance, [Unity AI Gateway](/concepts/unity-ai-gateway.md) provides a central control plane for governing AI traffic—including LLM endpoints and MCP servers—across an organization. This is a separate but complementary capability to the asset-based governance described above. ^[ai-governance-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform underlying all securable assets
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Policies that can grant access based on tags
- [ABAC GRANT Policies](/concepts/abac-grant-policies.md) — Dynamic permission policies using governed tags
- MLflow Models — The model registry used for Unity Catalog models
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Endpoints for Databricks-hosted models
- [Unity AI Gateway](/concepts/unity-ai-gateway.md) — Enterprise control plane for AI traffic governance

## Sources

- ai-governance-databricks-on-aws.md

# Citations

1. [ai-governance-databricks-on-aws.md](/references/ai-governance-databricks-on-aws-e6fd4910.md)

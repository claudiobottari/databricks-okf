---
title: AI governance | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/ai-governance
ingestedAt: "2026-06-18T08:03:53.434Z"
---

AI governance extends the data governance capabilities of Unity Catalog to AI resources, applying the same access control, lineage, and audit model that protects your data assets to your AI assets and AI traffic.

## AI asset governance with Unity Catalog[​](#ai-asset-governance-with-unity-catalog "Direct link to AI asset governance with Unity Catalog")

Unity Catalog manages AI assets as securable objects. You can grant and revoke access to the following AI assets using standard Unity Catalog privileges:

*   **Models**: Registered ML models in Unity Catalog. See [Manage model lifecycle](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/).
*   **Functions**: Unity Catalog functions used as agent tools or for data transformations. See [Create AI agent tools using Unity Catalog functions](https://docs.databricks.com/aws/en/generative-ai/agent-framework/create-custom-tool).
*   **Connections**: Unity Catalog HTTP connections used to access external APIs and MCP servers. See [HTTP connections](https://docs.databricks.com/aws/en/query-federation/http).
*   **Hosted foundation models**: Databricks-hosted foundation models available through Foundation Model APIs. See [Foundation model Unity Catalog permissions](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/model-uc-permissions).

## AI traffic governance with Unity AI Gateway[​](#ai-traffic-governance-with-unity-ai-gateway "Direct link to ai-traffic-governance-with-unity-ai-gateway")

Beta

This feature is in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types). Account admins can control access to this feature from the account console **Previews** page. See [Manage Databricks previews](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews).

[Unity AI Gateway](https://docs.databricks.com/aws/en/ai-gateway/) is the enterprise control plane for governing AI traffic across your organization. Use Unity AI Gateway to manage and monitor LLM endpoints and MCP servers from a central location:

*   **LLMs**: Control access to hosted and external LLM endpoints, enforce rate limits, and track usage and costs across providers.
*   **MCPs**: Manage access to managed, external, and custom MCP servers alongside your LLM endpoints.

See [Unity AI Gateway](https://docs.databricks.com/aws/en/ai-gateway/).
